from antlr4 import CommonTokenStream, InputStream
from FunctionCallLexer import FunctionCallLexer
from FunctionCallParser import FunctionCallParser
from Function import Function
from StdinLineStream import StdinLineStream
from Signal import Signal, Status


class Computer:
    def set_function_processor(self, function_processor):
        self.function_processor = function_processor
    
    def set_fs_root(self, fs_root):
        self.fs_root = fs_root
    
    def execute(self, text):
        lexer = FunctionCallLexer(text)
        stream = CommonTokenStream(lexer)
        parser = FunctionCallParser(stream)

        statement = parser.statement().function()

        if (statement):
            function = Function(statement)
            tree = function.process_statement_tree()
            return self.function_processor.evaluate_statement_tree(tree)
        else:
            return Status.OK
    
    def boot(self):
        with open(f'{self.fs_root}/boot.fosl', 'r') as bootloader:
            lines = bootloader.readlines()
            for line in lines:
                self.execute(InputStream(line))
    
    def command_loop(self, prompt='$ '):
        while (True):
            print(prompt, end='', flush=True)
            text = StdinLineStream()
            output = self.execute(text)

            if (output.value == Signal.TERM_EXIT):
                break