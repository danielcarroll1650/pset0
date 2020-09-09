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
        #raise NotImplementedError()
        self.initial = initial
        self.working_list = []
        for i in self.initial:
            self.working_list.append(i)
        
    def __call__(self, i):
        #raise NotImplementedError()
        self.counter = i - len(self.working_list)
        self.first_add = sum(self.initial) #23
        self.working_list.append(self.first_add) #working_list = [5,7,11,23]
        self.counter -= 1 #Missing piece in answer key's code, will get correct answer if this is deleted
        
        while self.counter != 0:
            self.working_list.pop(0) #working_list = [7,11,23]
            additive = sum(self.working_list) #41
            self.working_list.append(additive) #working_list = [7,11,23,41]
            self.counter -= 1
        return self.working_list[-1]

if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(4)))