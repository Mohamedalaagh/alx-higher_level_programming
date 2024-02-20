#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] in my_list[0:i]:
            continue
        else:
            sum += my_list[i]
    return sum
