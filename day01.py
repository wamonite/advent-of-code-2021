#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_inc_1():
    last = None
    count = 0
    with open('data/day01.txt') as file_object:
        for line in file_object.readlines():
            val = int(line.strip())
            if last is not None and val > last:
                count += 1
            last = val
    print(count)


def find_inc_2():
    last = None
    vals = []
    val = None
    count = 0
    with open('data/day01.txt') as file_object:
        for line in file_object.readlines():
            current = int(line.strip())
            vals.append(current)
            if len(vals) == 4:
                vals.pop(0)
            if len(vals) == 3:
                val = vals[0] + vals[1] + vals[2]
            if last is not None and val > last:
                count += 1
            last = val
    print(count)


def run():
    find_inc_1()
    find_inc_2()


if __name__ == "__main__":
    run()
