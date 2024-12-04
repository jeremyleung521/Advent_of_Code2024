# Day2.py
#
# First attempt at doing Day 2 of Advent of Code 2024

import time
import numpy


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_count = [[int(val) for val in line.split()] for line in read_list]

    return final_count


def check_if_good(input):
    check = 0
    for val_a, val_b in zip(input[:-1], input[1:]):
        diff = val_a - val_b
        direction = -1 if diff > 0 else 1
        if 0 < abs(diff) <= 3:
            if check == 0:
                if diff > 0:
                    check -= 1
                else:
                    check += 1
            elif check != direction:
                return 0
        else:
            return 0
    return 1

def check_if_tolerable(input, nested=False):
    check = 0
    #print(f'input: {input}')

    for idx, (val_a, val_b) in enumerate(zip(input[:-1], input[1:])):
        #print(val_a, val_b)
        diff = val_a - val_b
        direction = -1 if diff > 0 else 1

        if check == 0:
            if diff > 0:
                check -= 1
            else:
                check += 1

        if 0 < abs(diff) <= 3:
            if check != direction:
                if not nested:
                    tolerable = input.copy()
                    tolerable.pop(idx+1)
                    if check_if_tolerable(tolerable, nested=True) == 1:
                        return 1
                    else:
                        tolerable = input.copy()
                        tolerable.pop(idx)
                        if check_if_tolerable(tolerable, nested=True) == 1:
                            return 1
                        else:
                            tolerable = input.copy()
                            tolerable.pop(0)
                            if check_if_tolerable(tolerable, nested=True) == 1:
                                return 1
                            else:
                                return 0
                else:
                    #print('blah')
                    return 0
        else:
            if not nested:
                tolerable = input.copy()
                tolerable.pop(idx + 1)
                if check_if_tolerable(tolerable, nested=True) == 1:
                    return 1
                else:
                    tolerable = input.copy()
                    tolerable.pop(idx)
                    if check_if_tolerable(tolerable, nested=True) == 1:
                        return 1
                    else:
                        tolerable = input.copy()
                        tolerable.pop(0)
                        if check_if_tolerable(tolerable, nested=True) == 1:
                            return 1
                        else:
                            return 0
            else:
                #print('blah2')
                return 0
    return 1


def main():
    ## Part 1
    #b = read_input("Day2_test_input.txt")
    b = read_input("Day2_input.txt")
    answer = 0
    for line in b:
        answer += check_if_good(line)
    print(f'{answer} good lines.')


def main2():
    # Part 2
    #a = read_input("Day2_test_input.txt")
    a = read_input("Day2_input.txt")
    #a = read_input("Day2_test_edge.txt")

    #a = [[8, 11, 14, 17, 19, 18, 19]]
    # a = [[29, 28, 27, 25, 26, 25, 22, 20]]
    #a = [[48, 46, 47, 49, 51, 54, 56]]
    # a = [[1, 4, 3, 2, 1,]]

    answer2 = 0
    for line in a:
        test = check_if_tolerable(line, False)
        #if test == 0:
        #    print(line)
        answer2 += test
    print(f'{answer2} good lines.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
