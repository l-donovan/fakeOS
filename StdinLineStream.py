import sys
from antlr4.InputStream import InputStream


class StdinLineStream(InputStream):
    def __init__(self):
        stdin_str = sys.stdin.readline()
        super(StdinLineStream, self).__init__(stdin_str)
