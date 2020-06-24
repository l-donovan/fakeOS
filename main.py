from antlr4 import *
from FunctionCallLexer import FunctionCallLexer
from FunctionCallParser import FunctionCallParser
from StdinLineStream import StdinLineStream
from Function import Function
from FunctionProcessor import FunctionProcessor

import calls

def main():
    text = StdinLineStream()
    lexer = FunctionCallLexer(text)
    stream = CommonTokenStream(lexer)
    parser = FunctionCallParser(stream)

    statement = parser.statement()
    function = Function(statement.function())
    tree = function.process_statement_tree()

    function_processor = FunctionProcessor()
    function_processor.register('mul', calls.mul)
    function_processor.register('add', calls.add)

    output = function_processor.evaluate_statement_tree(tree)
    print(output)

if __name__ == '__main__':
    main()