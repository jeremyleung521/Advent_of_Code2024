# Day5.py
#
# First attempt at doing Day 5 of Advent of Code 2024

import time
from tqdm.auto import tqdm, trange


def read_input(file_name):
    with open(file_name, 'r') as f:
        read_list = f.read().splitlines()

    rules = []
    updates = []
    master_rules = {}
    for line in read_list:
        if len(line) > 0:
            match line[2]:
                case "|":
                    temp = [int(number) for number in line.split('|')]
                    rules.append(temp)
                    if temp[0] not in master_rules:
                        master_rules[temp[0]] = {temp[1]}
                    else:
                        master_rules[temp[0]].add(temp[1])
                case ",":
                    updates.append([int(number) for number in line.split(',')])

    # master_rules is a set that has all the previous numbers + more
    # master_rules = {a2: set(b for b, a in rules if a == a2) for a2 in set(a for b, a in rules)}
    for sub_a in set(after for before, after in rules):
        temp = set()
        for before, after in rules:
            if after == sub_a:
                temp.add(before)

        master_rules[sub_a] = temp

    # print([len(val) for val in master_rules.values()])
    # master_rules = dict(sorted(master_rules.items(), key=lambda item: len(master_rules) - len(item[1])))
    return rules, updates, master_rules


def check(rule, updates, good):
    for line_num, line in enumerate(updates):
        if rule[0] in line and rule[1] in line:
            line_copy = line.copy()

            while True:
                try:
                    left_pos = line_copy.index(rule[0])
                    right_post = line_copy.index(rule[1])
                    if left_pos > right_post:
                        raise IndexError

                    line_copy.pop(line_copy.index(rule[0]))

                except IndexError:
                    good[line_num] = False
                    break
                except ValueError:
                    break

    return good


def return_middle(line, rules=None):
    if rules is not None:
        # Reorder things

        # print(f'before: {line}')

        line = sorted(line, key=lambda x: sum(b in rules.get(x, set()) for b in line))

        #
        # tracker = line.copy()
        # new_line = []
        # for key in rules:
        #     if key in line:
        #         times = line.count(key)
        #         for _ in range(times):
        #             new_line.append(key)
        #             tracker.pop(tracker.index(key))
        #
        # for chara in tracker:
        #     new_line.append(chara)
        #
        # assert len(new_line) == len(line)
        #
        # line = new_line
        #
        # good.append(line)
        # print(f'after: {line}')

    # print(len(line))
    # print(int(len(line)/2))
    pos = len(line) // 2
    return line[pos]


def main():
    # Part 1 + 2
    # rules, updates, master_rules = read_input("Day5_test_input.txt")
    rules, updates, master_rules = read_input("Day5_input.txt")

    good = [True for _ in range(len(updates))]
    for rule in tqdm(rules):
        check(rule, updates, good)

    count = sum(good)

    count2 = len(good) - count

    answer, answer2 = 0, 0
    for idx, pos in enumerate(good):
        match pos:
            case True:
                # Part 1
                answer += return_middle(updates[idx])
            case False:
                # Part 2
                answer2 += return_middle(updates[idx], rules=master_rules)

    # print(master_rules)

    print(f'{count} good lines with sum {answer}.')
    print(f'{count2} bad lines with sum {answer2}.')


if __name__ == "__main__":
    ## Part 1 + 2
    startTime = time.perf_counter()
    main()
    print(f'{time.perf_counter() - startTime} sec.')
