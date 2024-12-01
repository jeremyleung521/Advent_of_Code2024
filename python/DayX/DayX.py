# DayX.py
#
# First attempt at doing Day X of Advent of Code 2023

import time
import numpy


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    final_count = [0]
    counter = 0
    for entry in read_list:
        if entry != '':
            final_count[counter] += int(entry)
        else:
            counter += 1
            final_count.append(0)

    final_count = numpy.asarray(final_count)

    return final_count


def return_max(input_list):
    max_cal = numpy.max(input_list)
    where = numpy.where(input_list == max_cal)[0][0]

    return [int(max_cal), where]


def return_top3(input_list):
    sorted_list = sorted(input_list, key=lambda x: -x)
    cal_sum = sum(sorted_list[0:3])
    where_three = numpy.where(input_list > sorted_list[3])[0]

    return [int(cal_sum), where_three]


def main():
    ## Part 1
    b = read_input("DayX_test_input.txt")
    # b = read_input("DayX_input.txt")
    answer = return_max(b)
    print(f'Elf {answer[1]+1} has {answer[0]} calories worth of food.')


def main2():
    # Part 2
    a = read_input("DayX_test_input.txt")
    # a = read_input("DayX_input.txt")
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
