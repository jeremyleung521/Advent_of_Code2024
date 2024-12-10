# Day10.py
#
# First attempt at doing Day 10 of Advent of Code 2024

import time
import numpy as np
from collections import deque

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    output_list = [list(line) for line in read_list]

    nine_locations = {(row, column) for row in range(len(output_list)) for column in range(len(output_list[0])) if output_list[row][column] == '9'}
    zero_locations = {(row, column) for row in range(len(output_list)) for column in range(len(output_list[0])) if output_list[row][column] == '0'}

    return output_list, nine_locations, zero_locations

movements = {(0,1), (1,0), (0, -1), (-1,0)}

def trace_trailhead(mapping, nine_locations, zero_locations):
    max_coord = len(mapping)
    coords_to_check = deque()
    next_to_check = []
    trail_counter = {coord: 0 for coord in zero_locations}
    number_counter = 0


    for positions in zero_locations:
        coords_to_check.append(positions)
        next_to_check = deque()
        success = []
        for number in range(10):
            # print(f'NUMBER {number=}')
            # print(f'{coords_to_check=}')
            for coord in list(coords_to_check):
                # print(coords_to_check)
                coords_to_check.popleft()
                for movement in movements:
                    test_position = (coord[0] + movement[0], coord[1] + movement[1])
                    # print(test_position)
                    if (0 <= test_position[0] < max_coord) and (0 <= test_position[1] < max_coord):
                        if mapping[test_position[0]][test_position[1]] == str(number + 1):
                            # print('yes')
                            next_to_check.append(test_position)
                            if number == 8 and test_position in nine_locations and test_position not in success:
                                # print('bowwow', test_position)
                                trail_counter[positions] += 1
                                success.append(test_position)

                #if number == 8:
                #    print(f'{next_to_check=}')
                #    for _ in range(len(next_to_check)):

            if len(coords_to_check) == 0:
                coords_to_check = deque(next_to_check)
                next_to_check = []

        # print(f'{trail_counter=}')
        # print(nine_locations)

    return trail_counter, sum(trail_counter.values()), len(trail_counter.keys())


def main():
    ## Part 1
    # a, nine, zero = read_input("Day10_test_input.txt")
    a, nine, zero = read_input("Day10_input.txt")

    answer = trace_trailhead(a, nine, zero)
    print(f'{answer[2]} trailheads with sum {answer[1]} .')


def main2():
    # Part 2
    b = read_input("Day10_test_input.txt")
    # b = read_input("Day10_input.txt")
    answer2 = return_top3(b)
    print(f'Elves {answer2[1] + 1} have {answer2[0]} calories worth of food.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    # startTime = time.perf_counter()
    # main2()
    # print(f'{time.perf_counter() - startTime} sec.')
