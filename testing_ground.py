def three_fib(input_len=100000,input_list=[5,7,11]):
    counter = input_len -4 #5
    working_list = input_list #[5,7,11]
    first_add = sum(input_list) #23
    working_list.append(first_add) #working_list = [5,7,11,23]
    while counter != 0:
        working_list.pop(0) #working_list = [7,11,23]
        additive = sum(working_list) #41
        working_list.append(additive) #working_list = [7,11,23,41]
        counter -= 1 #0
    
    working_list.pop(0)

    input_num = str(working_list[-1])
    final_number = input_num[-8:]
    print(int(final_number))

three_fib()