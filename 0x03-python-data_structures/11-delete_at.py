#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if idx >= 0 and idx < len(my_list):
            for i in range(len(my_list)):
                if (idx == i):
                    my_list.remove(i + 1)
                    return my_list
    return my_list
