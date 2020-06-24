from functools import reduce
import operator

def mul(args):
    return reduce(operator.mul, [float(arg.value) for arg in args], 1)

def add(args):
    return sum([float(arg.value) for arg in args])