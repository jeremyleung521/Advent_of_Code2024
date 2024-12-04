# Day4.py
#
# First attempt at doing Day 4 of Advent of Code 2024

import time
import numpy as np


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return np.asarray([list(line) for line in read_list])


def move(input_list, row_id, column_id, max_size=137):
    return {'u' : [input_list[row_id - 1, column_id], input_list[row_id - 2, column_id],
                   input_list[row_id - 3, column_id]] if row_id > 2 else None,
            'ur': [input_list[row_id - 1, column_id + 1], input_list[row_id - 2, column_id + 2],
                   input_list[row_id - 3, column_id + 3]] if row_id > 2 and column_id < max_size else None,
            'r' : [input_list[row_id, column_id + 1], input_list[row_id, column_id + 2],
                   input_list[row_id, column_id + 3]] if column_id < max_size else None,
            'dr': [input_list[row_id + 1, column_id + 1], input_list[row_id + 2, column_id + 2],
                   input_list[row_id + 3, column_id + 3]] if row_id < max_size and column_id < max_size else None,
            'd' : [input_list[row_id + 1, column_id], input_list[row_id + 2, column_id],
                   input_list[row_id + 3, column_id]] if row_id < max_size else None,
            'dl': [input_list[row_id + 1, column_id - 1], input_list[row_id + 2, column_id - 2],
                   input_list[row_id + 3, column_id - 3]] if row_id < max_size and column_id > 2 else None,
            'l' : [input_list[row_id, column_id - 1], input_list[row_id, column_id - 2],
                   input_list[row_id, column_id - 3]] if column_id > 2 else None,
            'ul': [input_list[row_id - 1, column_id - 1], input_list[row_id - 2, column_id - 2],
                   input_list[row_id - 3, column_id - 3]] if column_id > 2 and row_id > 2 else None,}

def move_X(input_list, row_id, column_id, max_size=138):
    possible_cross = [['M', 'S'], ['S', 'M']]
    if 0 < row_id < max_size and 0 < column_id < max_size:
        if (([input_list[row_id - 1, column_id - 1], input_list[row_id + 1, column_id + 1]] in possible_cross)
                and ([input_list[row_id + 1, column_id - 1], input_list[row_id - 1, column_id + 1]] in possible_cross)):
            return 1
        else:
            return 0
    else:
        return 0


def navigate(input_list):
    input_shape = len(input_list)
    count = 0
    x_count = 0
    for row_id, line in enumerate(input_list):
        for column_id, character in enumerate(line):
            match character:
                case 'X':
                    possible = move(input_list, row_id, column_id, max_size=input_shape-3)
                    for key, val in possible.items():
                        match val:
                            case ['M', 'A', 'S']:
                                count += 1
                            case None:
                                pass
                case 'A':
                    x_count += move_X(input_list, row_id, column_id, max_size=input_shape-1)
                case _:
                    continue

    return count, x_count


def main():
    ## Part 1
    #b = read_input("Day4_test_input.txt")
    b = read_input("Day4_input.txt")
    answer, answer2 = navigate(b)
    print(f'{answer} instances of XMAS.')
    print(f'{answer2} instances of X-MAS.')


if __name__ == "__main__":
    ## Part 1 + 2
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')
