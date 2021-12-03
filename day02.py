#!/usr/bin/env python
# -*- coding: utf-8 -*-


CMD_LOOKUP = {
    'up': (0, -1),
    'down': (0, 1),
    'forward': (1, 0),
}


def find_pos_1():
    x, y = (0, 0)
    with open('data/day02.txt') as file_object:
        for line in file_object.readlines():
            cmd, step = line.strip().split(' ')
            step = int(step)
            x_step, y_step = CMD_LOOKUP[cmd]
            x += x_step * step
            y += y_step * step
    print(x * y)


def find_pos_2():
    x, y, aim = (0, 0, 0)
    with open('data/day02.txt') as file_object:
        for line in file_object.readlines():
            cmd, val = line.strip().split(' ')
            val = int(val)
            x_step, y_step = CMD_LOOKUP[cmd]
            x += x_step * val
            aim += y_step * val
            if x_step:
                y += aim * val
    print(x * y)


def run():
    find_pos_1()
    find_pos_2()


if __name__ == "__main__":
    run()
