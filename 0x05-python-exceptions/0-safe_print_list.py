#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end='')
            counter++
        except IndexError:
            pass
    print('please try again')
    return counter
