# Day8.py
#
# First attempt at doing Day 8 of Advent of Code 2024

import time
import numpy as np
from itertools import permutations


def read_input(file_name: str):
    # Processing the file into a list of list of strings
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    return_list = [list(line) for line in read_list]

    # Tracking all the frequencies
    unique_frequencies = set()
    [unique_frequencies.update(set(line)) for line in return_list]
    unique_frequencies.remove('.')
    unique_frequencies = {frequency: set() for frequency in unique_frequencies}

    # Finding all coordinates of each unique frequency
    [unique_frequencies[frequency].add((y_idx, x_idx)) for frequency in unique_frequencies
     for y_idx, line in enumerate(return_list) for x_idx, chara in enumerate(line) if chara == frequency]

    # return mapping, all the unique frequencies + coordinates and the shape of the mapping
    return return_list, unique_frequencies, [len(return_list), len(return_list[0])]


def gen_all_antinodes(mapping: list, unique_frequencies: dict, shape_of_mapping: list):
    antinodes = {}

    for frequency, coordinates in unique_frequencies.items():
        antinodes[frequency] = set((2 * x[0] - y[0], 2 * x[1] - y[1]) for x, y in permutations(coordinates, 2))

        # Removing any antinodes that are out of bounds
        [antinodes[anti_freq].remove(pop_coord) for anti_freq, anti_coord in antinodes.items() for pop_coord in list(anti_coord) if not ((0 <= pop_coord[0] < shape_of_mapping[0]) and (0 <= pop_coord[1] < shape_of_mapping[1]))]

    master_antinodes = set()
    [master_antinodes.update(anti_coords) for anti_coords in antinodes.values()]

    return antinodes, len(master_antinodes)


def gen_resonant_nodes(mapping: list, unique_frequencies: dict, shape_of_mapping: list):
    antinodes = {}

    for frequency, coordinates in unique_frequencies.items():
        antinodes[frequency] = set()
        for x, y in permutations(coordinates, 2):
            x_diff, y_diff = x[0] - y[0], x[1] - y[1]
            curr_x, curr_y = x[0], x[1]
            while True:
                curr_x -= x_diff
                curr_y -= y_diff

                if 0 <= curr_x < shape_of_mapping[0] and 0 <= curr_y < shape_of_mapping[1]:
                    antinodes[frequency].add((curr_x, curr_y))
                else:
                    break

    master_antinodes = set()
    [master_antinodes.update(anti_coords) for anti_coords in antinodes.values()]

    return antinodes, len(master_antinodes)


def main():
    ## Part 1
    # mapping, freq, shape = read_input("Day8_test_input.txt")
    mapping, freq, shape = read_input("Day8_input.txt")
    antinodes, answer = gen_all_antinodes(mapping, freq, shape)
    print(f'{answer} antinodes.')


def main2():
    ## Part 2
    # mapping, freq, shape = read_input("Day8_test_input.txt")
    mapping, freq, shape = read_input("Day8_input.txt")
    antinodes, answer2 = gen_resonant_nodes(mapping, freq, shape)
    print(f'{answer2} antinodes.')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
