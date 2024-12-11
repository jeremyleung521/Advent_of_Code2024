# Day11.py
#
# First attempt at doing Day 11 of Advent of Code 2024

import time
from tqdm.auto import tqdm, trange


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()[0].split(' ')


    return [int(s) for s in read_list]

cache = {'0': ('1',)}

def blink(input_list):
    new_list = []
    for number in input_list:
        if number in cache:
            [new_list.append(val) for val in cache[number]]
        elif number == '0':
            new_list.append('1')
        elif len(number) % 2 == 0:
            length = int(len(number) / 2)
            calc_a = str(int(number[:length]))
            calc_b = str(int(number[length:]))
            new_list.append(calc_a)
            new_list.append(calc_b)
            cache[number] = (calc_a, calc_b)
        else:
            calc = str(int(number) * 2024)
            new_list.append(calc)
            cache[number] = (calc,)

    return new_list



def blink2(input_list, times=25):
    cache = {'0': ['0']}
    for _ in trange(25, desc='cache', leave=False):
        cache['0'] = blink(cache['0'])
        # print(cache)
    count = 0
    final_list = []
    print(len(input_list))
    for number in tqdm(input_list, desc='total_times'):
        new_list = [number]

        if number in cache:
            boop = []
            for new_number in cache[number]:
                new_number = [new_number]
                for _ in range(2):
                    new_number = blink(new_number)
                    [boop.append(val) for val in new_number]

            count += len(boop)
        else:
            for i in trange(times, desc=f'{times}', leave=False):
                new_new_list = []
                if number in cache:
                    for _ in range(3):
                        final_list.append(cache[number])
                    count += len(cache[number])
                    break
                else:
                    for value in new_list:
                        if value == '0':
                            new_new_list.append('1')
                        elif len(value) % 2 == 0:
                            length = int(len(value) / 2)
                            calc_a = str(int(value[:length]))
                            calc_b = str(int(value[length:]))
                            new_new_list.append(calc_a)
                            new_new_list.append(calc_b)
                        else:
                            calc = str(int(value) * 2024)
                            new_new_list.append(calc)
                    if i == times-1:
                        cache[number] = new_new_list

                new_list = new_new_list

                if i == times-1:
                    count += len(new_list)
                    final_list.append(new_list)

    #print(cache)
    #print(final_list)

    return count



def main(times=25):
    ## Part 1
    #a = read_input("Day11_test_input.txt")
    a = read_input("Day11_input.txt")
    answer = a
    print(f'Starting with {a} .')
    for i in trange(times):
        answer = blink2(answer)
        # print(f'After {i+1} blink(s) is {answer} .')

    print(f'There would be {len(answer)} stones at the end.')


def main2():
    ## Part 2
    # a = read_input("Day11_test_input.txt")
    a = read_input("Day11_input.txt")
    answer = a
    print(f'Starting with {a} .')

    for i in trange(75):
        answer = blink(answer)

    # answer2 = blink2(answer, 45)
    # print(f'After {i+1} blink(s) is {answer} .')

    print(f'There would be {len(answer)} stones at the end.')


if __name__ == "__main__":
    ## Part 1
    # startTime = time.perf_counter()
    # main()
    # print(f'{time.perf_counter() - startTime} sec.')

    ## Part 2
    startTime = time.perf_counter()
    main2()
    print(f'{time.perf_counter() - startTime} sec.')

