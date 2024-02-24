#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    divided_by = 0
    for i in my_list:
        sum += i[0] * i[1]
        divided_by += i[1]
    return sum / divided_by
