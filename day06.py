#!/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import Counter


def load_data(test):
    with open(f"data/day06{'_test' if test else ''}.txt") as file_object:
        return list(map(int, file_object.readline().strip().split(',')))


def run_gen_1(generations, test = False):
    age_list = load_data(test)
    age_count = Counter(age_list)
    for idx in range(generations):
        new_members = age_count[0]
        age_count = Counter({age - 1: ac for age, ac in age_count.items() if age > 0})
        age_count.update({6: new_members})
        age_count.update({8: new_members})

    print(sum(age_count.values()))


def run():
    run_gen_1(80, True)
    run_gen_1(80)
    run_gen_1(256, True)
    run_gen_1(256)


if __name__ == "__main__":
    run()
