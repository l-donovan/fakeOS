from functools import reduce
from Signal import Signal, Status
import operator

# TODO temporary solution
database = {}


def add(args):
    return sum([float(arg.value) for arg in args])


def sub(args):
    return float(args[0].value) + sum([-float(arg.value) for arg in args[1:]])


def mul(args):
    return reduce(operator.mul, [float(arg.value) for arg in args], 1)


def div(args):
    return float(args[0].value) / float(args[1].value)


def set(args):
    database[args[0].value] = args[1]
    return Status.OK


def get(args):
    return float(database[args[0].value].value)


def unset(args):
    key = args[0].value

    if (key in database):
        del database[key]
        return Status.OK
    else:
        return Status.BAD


def exit(args):
    return Signal.TERM_EXIT


def qprint(args):
    print(*[arg.value for arg in args], flush=True)
    return Status.OK
