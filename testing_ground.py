def three_fib(input_len=8,input_list=[5,7,9]):
    counter = input_len #5
    working_list = input_list #[5,7,9]
    first_add = sum(input_list) #21
    working_list.append(first_add) #working_list = [5,7,9,21]
    counter -= 4 #1
    while counter != 0:
        working_list.pop(0) #working_list = [7,9,21]
        additive = sum(working_list) #37
        working_list.append(additive) #working_list = [7,9,21,37]
        counter -= 1 #0
    return working_list[-1]

print(three_fib())