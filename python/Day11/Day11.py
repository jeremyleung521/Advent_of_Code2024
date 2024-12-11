# Day11.py
#
# First attempt at doing Day 11 of Advent of Code 2024

import time
from tqdm.auto import tqdm, trange


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()[0].split(' ')

    return [int(s) for s in read_list]


def blink(input_list):
    new_list = []
    for number in input_list:
        if number == 0:
            new_list.append(1)
        elif len(str(number)) % 2 == 0:
            length = int(len(str(number)) / 2)
            calc_a = int(str(number)[:length])
            calc_b = int(str(number)[length:])
            new_list.append(calc_a)
            new_list.append(calc_b)
        else:
            calc = number * 2024
            new_list.append(calc)

    return new_list


def main(times=25):
    ## Part 1
    #a = read_input("Day11_test_input.txt")
    a = read_input("Day11_input.txt")
    answer = a
    print(f'Starting with {a} .')
    for i in trange(times, leave=False):
        answer = blink(answer)
        # print(f'After {i+1} blink(s) is {answer} .')

    print(f'There would be {len(answer)} stones at the end.')


new_cache = {0: (1,)}

def new_blink(number):
    if number in new_cache:
        return new_cache[number]
    string = str(number)
    if len(string) % 2 == 0:
        length = int(len(string) / 2)
        calc = (int(str(number)[length:]), int(str(number)[:length]))
    else:
        calc = (number * 2024,)

    new_cache[number] = calc

    return calc


def main2():
    ## Part 2
    # a = read_input("Day11_test_input.txt")
    a = read_input("Day11_input.txt")
    print(f'Starting with {a} .')

    stone_count = {stone: a.count(stone) for stone in a}

    times = 75

    for i in range(1,times+1):
        new_count = {}
        for stone, count in stone_count.items():
            for new_stone in new_blink(stone):
                new_count[new_stone] = new_count.get(new_stone, 0) + count
        stone_count = new_count

        if i in [times]:
            # print(stone_count)
            print(sum(stone_count.values()))


if __name__ == "__main__":
    ## Part 1
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')

