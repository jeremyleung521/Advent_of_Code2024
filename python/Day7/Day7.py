# Day7.py
#
# First attempt at doing Day 7 of Advent of Code 2024

import time
import numpy as np
from itertools import product

def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def concatenation(a, b):
    return int(str(a) + str(b))


operators = [addition, multiplication, concatenation]
operator_names = ['+', '*', '||']

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return [[int(line.split(': ')[0]), [int(number) for number in line.split(': ')[1].split(' ')]] for line in read_list]


def process(result, values, concatenation=False):
    possible_operators = [0, 1, 2] if concatenation else [0, 1]
    for set_of_operators in product(possible_operators, repeat=len(values)-1):
        test_count = values[0]
        performed_calc= f'{values[0]}'
        for op_id, number in enumerate(values[1:]):
            test_count = operators[set_of_operators[op_id]](test_count, number)
            performed_calc = f'{performed_calc} {operator_names[set_of_operators[op_id]]} {number}'

        if test_count == result:
            # print(f'{performed_calc} = {test_count}, {result}')
            return result

    return 0


def main():
    ## Part 1
    #b = read_input("Day7_test_input.txt")
    b = read_input("Day7_input.txt")

    answer = 0
    for line in b:
        answer += process(line[0], line[1])
    print(f'{answer} is the sum.')


def main2():
    # Part 2
    #a = read_input("Day7_test_input.txt")
    a = read_input("Day7_input.txt")
    answer2 = 0
    for line in a:
        answer2 += process(line[0], line[1], concatenation=True)
    print(f'{answer2} is the sum')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
