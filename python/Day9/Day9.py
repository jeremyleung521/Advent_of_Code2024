# Day9.py
#
# First attempt at doing Day 9 of Advent of Code 2024

import time
import numpy as np
from collections import deque
from itertools import cycle

def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = deque(f.read())

    parity = cycle([0,1])
    if len(read_list) % 2 == 0:
        next(parity)
    # 1 is free space
    # 0 is data

    return read_list, parity


def compact_line_t2(input_list, parity):
    output_list = []
    data_id = 0
    for iloc, times in enumerate(input_list):
        match next(parity):
            case 0:
                for i in range(int(times)):
                    output_list.append(data_id)
                data_id += 1
            case 1:
                for i in range(int(times)):
                    output_list.append('.')

    pos = len(output_list) - 1
    output_list_copy = output_list.copy()
    for idx, value in enumerate(output_list_copy):
        #while idx < pos:
        match value:
            case '.':
                while output_list[pos] == '.':
                    pos -= 1
                output_list[idx] = output_list[pos]
                output_list[pos] = '.'

        # print(idx, pos)
        # print(output_list)
        if idx == pos:
            break

    # print(output_list)

    answer_sum = 0
    for idx, chara in enumerate(output_list):
        if chara != '.':
            answer_sum += idx * int(chara)

    return answer_sum


def compact_line(input_list, parity):
    final_str_list = []
    final_file_number = str(int(len(input_list) / 2))
    input_list_copy = list(input_list)
    expected_length = sum([int(i) if idx % 2 == 0 else 0 for idx, i in enumerate(input_list)])

    while len(input_list) > 0:
        try:
            for idx, val in enumerate(input_list_copy):
                # print(final_str_list, idx)
                match idx % 2:
                    case 0:
                        for _ in range(int(val)):
                            final_str_list.append(str(int(idx / 2)))

                        # print(input_list)
                        if len(input_list) > 1:
                            input_list.popleft()
                        else:
                            for _ in range(int(input_list[-1])):
                                final_str_list.append(final_file_number)


                    case 1:
                        match next(parity):
                            case 1:
                                if len(input_list) > 0:
                                    input_list.pop()
                                else:
                                    for _ in range(input_list[-1]):
                                        final_str_list.append(final_file_number)
                                #print(f'{next(parity)=}')

                        for _ in range(int(val)):
                            # print(final_str_list)
                            # print(input_list[-1])
                            # for _ in range(int(input_list[-1])):
                            if int(input_list[-1]) > 0:
                                final_str_list.append(final_file_number)
                            else:
                                # print('exception')
                                final_file_number = str(int(final_file_number) - 1)
                                final_str_list.append(final_file_number)

                                input_list.pop()
                                input_list.pop()
                                # final_idx -= 2
                                next(parity)

                            input_list[-1] = str(int(input_list[-1]) - 1)

                            if int(input_list[-1]) == 0:
                                final_file_number = str(int(final_file_number) - 1)
                                input_list.pop()
                                input_list.pop()
                                next(parity)


                        input_list.popleft()
        except IndexError:
            for _ in range(expected_length - len(final_str_list)):
                final_str_list.append(str(int(final_file_number) + 1))
            # print(f'{input_list=}')

            return final_str_list
            #return [final_str + next_str for next_str in final_str_list]

    #return [final_str + next_str for next_str in final_str_list]


def main():
    ## Part 1
    # input_list, parity = read_input("Day9_test_input.txt")
    input_list, parity= read_input("Day9_input.txt")

    expected_length = sum([int(i) if idx % 2 == 0 else 0 for idx, i in enumerate(input_list)])

    answer = compact_line_t2(input_list, parity)
    # answer = compact_line(input_list, parity)
    # answer_str = ''
    # for next_str in answer:
    #     answer_str += next_str
    # answer_str += '3'
    #
    # answer_sum = 0
    # for idx, chara in enumerate(answer):
    #     answer_sum += idx * int(chara)
    #
    print(f'{answer} .')
    # print(f'{expected_length=}')
    # print(f'{len(answer)=}')
    # print(f'{answer_sum} .')
    #print(f'Elf {answer[1]+1} has {answer[0]} calories worth of food.')


def main2():
    # Part 2
    b = read_input("Day9_test_input.txt")
    # b = read_input("Day9_input.txt")
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
