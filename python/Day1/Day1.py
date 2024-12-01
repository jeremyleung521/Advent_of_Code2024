# Day1.py
#
# First attempt at doing Day 1 of Advent of Code 2023

import time
import numpy


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    line_list = [line.split()  for line in read_list]

    left = [int(line[0]) for line in line_list]
    right = [int(line[1]) for line in line_list]

    return sorted(left), sorted(right)


def return_diff(left, right):
    diff_sum = 0
    for x,y in zip(left, right):
        diff_sum += abs(y - x)

    return diff_sum


def return_counts(right):
    dictionary = {}
    for number in right:
        dictionary[number] = right.count(number)

    return dictionary


def calc_similarity(left, dictionary):
    total_similarity = 0
    for value in left:
        try:
            total_similarity += value * dictionary[value]
        except KeyError:
            pass

    return total_similarity


def main():
    ## Part 1
    #a, b = read_input("Day1_test_input.txt")
    a, b = read_input("Day1_input.txt")
    answer = return_diff(a, b)
    print(f'Total difference is {answer} .')


def main2():
    # Part 2
    #a, b = read_input("Day1_test_input.txt")
    a, b = read_input("Day1_input.txt")
    dictionary = return_counts(b)
    answer2 = calc_similarity(a, dictionary)
    print(f'Similarity score is {answer2} .')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
