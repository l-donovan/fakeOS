from antlr4 import CommonTokenStream
from FunctionCallLexer import FunctionCallLexer
from FunctionCallParser import FunctionCallParser
from StdinLineStream import StdinLineStream
from Function import Function
from FunctionProcessor import FunctionProcessor
from Signal import Signal, Status
from Computer import Computer
import calls


def main():
    fn_processor = FunctionProcessor()
    fn_processor.register('mul',    calls.mul)
    fn_processor.register('add',    calls.add)
    fn_processor.register('sub',    calls.sub)
    fn_processor.register('div',    calls.div)
    fn_processor.register('get',    calls.get)
    fn_processor.register('set',    calls.set)
    fn_processor.register('unset',  calls.unset)
    fn_processor.register('exit',   calls.exit)
    fn_processor.register('quit',   calls.exit)
    fn_processor.register('print',  calls.qprint)
    fn_processor.register('format', calls.format)

    computer = Computer()
    computer.set_function_processor(fn_processor)
    computer.set_fs_root('./fakeOS_root')
    computer.boot()
    computer.command_loop()


if __name__ == '__main__':
    main()
