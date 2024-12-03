# Day3.py
#
# First attempt at doing Day 3 of Advent of Code 2023

import time
import numpy
import re

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().replace('\n', '')

    return read_list


def process_split(input):
    output = input.replace(')', 'mul(').replace('mul(', '_').split('_')
    good = []
    for frag_num, fragment in enumerate(output):
        try:
            a = fragment.split(',')
            if len(a) == 2:
                if ' ' in [chara for string in a for chara in string]:
                    raise ValueError
                good.append([frag_num, int(a[0]) * int(a[1]), fragment])
        except ValueError:
            pass

    return good


def process_split_do_dont(input):
    good = []
    results = []
    dont_split = input.split('don\'t()')

    good.append(dont_split[0])
    for block in dont_split[1:]:
        try:
            break_good = block.split('do()')[1:]
        except IndexError:
            continue

        for do_good in break_good:
            good += do_good.replace(')', 'mul(').replace('mul(', '_').split('_')

    for do_block in good:
        do_block_result = process_split(do_block)
        results.append(do_block_result)

    return results


def main():
    ## Part 1
    # b = read_input("Day3_test_input.txt")
    b = read_input("Day3_input.txt")
    returned_tuples = process_split(b)

    #returned_tuples = process_re(b)
    #print(len(returned_tuples))
    total_sum = 0
    for v in returned_tuples:
        total_sum += v[1]

    print(f'{total_sum} is the sum of products.')


def main2():
    # Part 2
    #a = read_input("Day3_test_input2.txt")
    a = read_input("Day3_input.txt")

    returned_tuples2 = process_split_do_dont(a)
    total_sum2 = 0
    for blah in returned_tuples2:
        for v in blah:
            total_sum2 += v[1]
    print(f'{total_sum2} is the sum of products.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
