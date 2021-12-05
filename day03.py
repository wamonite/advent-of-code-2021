#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import Counter


def find_power_consumption_1():
    one_counter = Counter()
    line_counter = 0
    with open('data/day03.txt') as file_object:
        for line in file_object.readlines():
            line = line.strip()

            idx = 0
            while line:
                ch, *line = line
                if ch == '1':
                    one_counter.update([idx])

                idx += 1

            line_counter += 1

    gamma = 0
    epsilon = 0
    for idx in range(len(one_counter)):
        gamma <<= 1
        epsilon <<= 1

        if one_counter[idx] > line_counter - one_counter[idx]:
            gamma |= 1
        else:
            epsilon |= 1

    print(f"{gamma} x {epsilon} = {gamma * epsilon}")


def process_digit(data, ones_win, idx = 0):
    if len(data) == 1:
        return int(data[0], 2)

    one_data = []
    zero_data = []
    one_count = 0
    for line in data:
        if line[idx] == '1':
            one_count += 1
            one_data.append(line)

        else:
            zero_data.append(line)

    one_won = one_count >= len(data) - one_count
    return process_digit(one_data if one_won == ones_win else zero_data, ones_win, idx + 1)


def find_power_consumption_2():
    data = []
    with open('data/day03.txt') as file_object:
        for line in file_object.readlines():
            line = line.strip()
            data.append(line)

    ogr = process_digit(data, True)
    csr = process_digit(data, False)
    print(f"{ogr} * {csr} = {ogr * csr}")


def run():
    find_power_consumption_1()
    find_power_consumption_2()


if __name__ == "__main__":
    run()
