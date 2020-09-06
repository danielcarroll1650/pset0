#!/usr/bin/env python3

#TestingGit

def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    #raise NotImplementedError()
    input_num = str(some_int)
    new_number = input_num[-8:]
    return int(new_number)

def optimized_fibonacci(f):
    #raise NotImplementedError()
    fib = [0,1]
    while len(fib) != f+1:
        finish = fib[-1] + fib[-2]
        fib.append(finish)
    return_value = fib[-1]
    return return_value

class SummableSequence(object):
    def __init__(self, *initial):
        raise NotImplementedError()

    def __call__(self, i):
        raise NotImplementedError()


if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
