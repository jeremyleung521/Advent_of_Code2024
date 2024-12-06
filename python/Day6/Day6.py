# Day6.py
#
# First attempt at doing Day 6 of Advent of Code 2024

import time
import numpy as np

directions = {'u': [-1, 0], 'r': [0, 1], 'd': [1, 0], 'l': [0, -1]}
cycle = list(directions)

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return np.asarray([list(line) for line in read_list])


def move(current_pos, mapping, direction=0):
    test_pos = tuple(a + b for a, b in zip(current_pos, directions[cycle[direction]]))

    try:
        match mapping[test_pos]:
            case '#':
                direction = (direction + 1) % 4
                test_pos = tuple(a + b for a, b in zip(current_pos, directions[cycle[direction]]))
            case _:  # '.' or '^' or 'X'
                pass
        mapping[test_pos] = 'X'
    except IndexError:
        pass

    return list(test_pos), direction


def main():
    ## Part 1
    #b = read_input("Day6_test_input.txt")
    b = read_input("Day6_input.txt")

    unique_coords = set()
    curr_pos = np.argwhere(b=='^')[0].tolist()
    direction = 0

    while (0 <= curr_pos[0] < len(b)) and (0 <= curr_pos[1] < len(b[0])):
        unique_coords.add(tuple(curr_pos))
        curr_pos, direction = move(curr_pos, mapping=b, direction=direction)

    answer = len(unique_coords)

    print(f'{answer} unique coordinates traversed.')


def main2():
    # Part 2
    a = read_input("Day6_test_input.txt")
    # a = read_input("Day6_input.txt")
    answer2 = return_top3(a)
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
