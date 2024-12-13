# Day13.py
#
# First attempt at doing Day 13 of Advent of Code 2024

import time
from unittest import case
from decimal import Decimal

import numpy as np


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    output = []
    a = []
    for line in read_list:
        if line != '':
            b = line.split(': ')
            c = b[1].split(', ')
            a.append((int(c[0][2:]), int(c[1][2:])))
            if len(a) == 3:
                output.append(a)
                a = []

    return output


def solve(a, b, r):
    ax, ay = a
    bx, by = b
    x, y = r

    A = (bx * y - by * x) / (ay * bx - ax * by)
    B = -(ax * y - ay * x) / (ay * bx - ax * by)

    return A, B


def calc_coins(line, add=0):
    cost = []
    total_cost = 0
    if add:
        add = 10000000000000

    for idx, (a, b, prize) in enumerate(line):
        A, B = solve(a, b, (prize[0] + add, prize[1] + add))
        curr_cost = 3 * A + B

        # cost.append([A, B, curr_cost])
        if np.isclose(float(Decimal(A) % 1), 0) and np.isclose(float(Decimal(B) % 1), 0):
            total_cost += curr_cost
            # print(f'{idx}: True, {cost[idx]}')
        else:
            pass
            # print(f'{idx}: False, {cost[idx]}')

    return cost, int(total_cost)


def main():
    ## Part 1
    # a = read_input("Day13_test_input.txt")
    a = read_input("Day13_input.txt")
    track, answer = calc_coins(a)
    print(f'{answer} is the total cost.')


def main2():
    # Part 2
    # b = read_input("Day13_test_input.txt")
    b = read_input("Day13_input.txt")
    track, answer2 = calc_coins(b, True)
    print(f'{answer2} is the total cost.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
