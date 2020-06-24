from antlr4 import *
from FunctionCallLexer import FunctionCallLexer
from FunctionCallParser import FunctionCallParser
from StdinLineStream import StdinLineStream
from Function import Function
from FunctionProcessor import FunctionProcessor
from Signal import Signal, Status

import calls


def greet():
    print('''\
  __      _         ____   _____ 
 / _|    | |       / __ \ / ____|
| |_ __ _| | _____| |  | | (___  
|  _/ _` | |/ / _ \ |  | |\___ \ 
| || (_| |   <  __/ |__| |____) |
|_| \__,_|_|\_\___|\____/|_____/ 
    ''')


def main():
    processor = FunctionProcessor()
    processor.register('mul',   calls.mul)
    processor.register('add',   calls.add)
    processor.register('sub',   calls.sub)
    processor.register('div',   calls.div)
    processor.register('get',   calls.get)
    processor.register('set',   calls.set)
    processor.register('unset', calls.unset)
    processor.register('exit',  calls.exit)
    processor.register('quit',  calls.exit)
    processor.register('print', calls.qprint)

    greet()

    while (True):
        print('$ ', end='', flush=True)
        text = StdinLineStream()
        lexer = FunctionCallLexer(text)
        stream = CommonTokenStream(lexer)
        parser = FunctionCallParser(stream)

        statement = parser.statement()
        function = Function(statement.function())
        tree = function.process_statement_tree()

        output = processor.evaluate_statement_tree(tree)

        if (output.value == Signal.TERM_EXIT):
            break


if __name__ == '__main__':
    main()
