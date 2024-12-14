# Day14.py
#
# First attempt at doing Day 14 of Advent of Code 2024

import time
import numpy as np


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    positions = []
    velocities = []
    for line in read_list:
        left, right = line.split(' ')
        pos = left.split(',')
        pos = (int(pos[0][2:]), int(pos[1]))
        vol = right.split(',')
        vol = (int(vol[0][2:]), int(vol[1]))

        positions.append(pos)
        velocities.append(vol)

    return positions, velocities


def print_picture(positions, xmax, ymax):
    mapping = np.zeros((xmax, ymax), dtype=int)
    for pos in positions:
        mapping[pos[0], pos[1]] += 1

    print(mapping)
    np.savetxt('output.txt', mapping, fmt='%1d')


def propagate(positions, velocities, xmax, ymax, steps=100, ncount=None):
    if ncount is None:
        ncount = steps
    for i in range(steps):
        new_positions = [((pos[0]+ vel[0]) % xmax, (pos[1]+ vel[1]) % ymax) for pos, vel in zip(positions, velocities)]
        positions = new_positions
        # print_picture(positions, xmax, ymax)

        if len(set(new_positions)) == ncount:
            print(i+1)
            print_picture(positions, xmax, ymax)
            break

    return positions


def count_quadrant(positions, xmax, ymax):
    quadrants = [0, 0, 0, 0]
    xdiv = xmax // 2
    ydiv = ymax //2
    for position in positions:
        x, y = position[0], position[1]
        if 0 <= x < xdiv and 0 <= y < ydiv:
            quadrants[0] += 1
        elif 0 <= x < xdiv and ydiv < y < ymax:
            quadrants[1] += 1
        elif (xdiv < x < xmax) and 0 <= y < ydiv:
            quadrants[2] += 1
        elif xdiv < x < xmax and ydiv < y < ymax:
            quadrants[3] += 1

    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return quadrants, safety_factor

def return_max(input_list):
    max_cal = np.max(input_list)
    where = np.where(input_list == max_cal)[0][0]

    return [int(max_cal), where]


def return_top3(input_list):
    sorted_list = sorted(input_list, key=lambda x: -x)
    cal_sum = sum(sorted_list[0:3])
    where_three = np.where(input_list > sorted_list[3])[0]

    return [int(cal_sum), where_three]


def main():
    ## Part 1
    # pos, vel = read_input("Day14_test_input.txt")
    pos, vel = read_input("Day14_input.txt")
    ncount = len(pos)
    # xmax, ymax = 11, 7  # example
    xmax, ymax = 101, 103  # real answer
    a = propagate(pos, vel, xmax, ymax, 100, ncount)
    quad, answer = count_quadrant(a, xmax, ymax)
    print(f'Safety score is {answer} .')


def main2():
    # Part 2
    # pos, vel = read_input("Day14_test_input.txt")
    pos, vel = read_input("Day14_input.txt")
    ncount = len(pos)
    # xmax, ymax = 11, 7  # example
    xmax, ymax = 101, 103  # real answer
    a = propagate(pos, vel, xmax, ymax, 100000, ncount)
    quad, answer = count_quadrant(a, xmax, ymax)
    print(f'Safety score is {answer} .')


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')
