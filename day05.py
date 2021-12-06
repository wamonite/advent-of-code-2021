#!/usr/bin/env python
# -*- coding: utf-8 -*-


from re import compile


def load_data(test):
    data = []
    matcher = compile(r'^(\d*),(\d*) *-> *(\d*),(\d*)\n$')
    with open(f"data/day05{'_test' if test else ''}.txt") as file_object:
        for line in file_object.readlines():
            match = matcher.match(line)
            if match:
                data.append(list(map(int, match.groups())))

    return data


def set_val(x, y, vent_lookup):
    vent_lookup.setdefault((x, y), 0)
    vent_lookup[(x, y)] += 1


def find_1(test = False):
    data = load_data(test)
    vent_lookup = {}
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                set_val(x1, y, vent_lookup)

        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                set_val(x, y1, vent_lookup)

    print(len([v for v in vent_lookup.values() if v >= 2]))


def find_2(test = False):
    data = load_data(test)
    vent_lookup = {}
    for x1, y1, x2, y2 in data:
        x = x1
        if x2 > x1:
            x_step = 1
        elif x2 < x1:
            x_step = -1
        else:
            x_step = 0

        y = y1
        if y2 > y1:
            y_step = 1
        elif y2 < y1:
            y_step = -1
        else:
            y_step = 0

        while True:
            set_val(x, y, vent_lookup)
            if x == x2 and y == y2:
                break
            x += x_step
            y += y_step

    print(len([v for v in vent_lookup.values() if v >= 2]))


def run():
    find_1(True)
    find_1()
    find_2(True)
    find_2()


if __name__ == "__main__":
    run()
