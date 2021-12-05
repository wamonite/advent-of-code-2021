#!/usr/bin/env python
# -*- coding: utf-8 -*-


from functools import reduce


def load_boards(board_lines):
    board = []
    for line in board_lines:
        line = line.strip()
        if not line:
            if board:
                yield board
            board = []

        else:
            board.append(list(map(int, line.split())))

    if board:
        yield board


def load_data(test):
    with open(f"data/day04{'_test' if test else ''}.txt") as file_object:
        data = file_object.readlines()

    calls = list(map(int, data[0].split(',')))
    boards = list(load_boards(data[1:]))

    return calls, boards


def mark_call(call, boards):
    for board in boards:
        for row in board:
            try:
                idx = row.index(call)
                row[idx] = -1
            except ValueError:
                pass


def test_won(board):
    for row in board:
        if all(map(lambda v: v < 0, row)):
            return True

    for idx in range(len(board[0])):
        if all(map(lambda v: v < 0, [r[idx] for r in board])):
            return True


def print_winner(call, board):
    unmarked = reduce(lambda l, r: max(l, 0) + max(r, 0), [v for r in board for v in r])
    print(f"{unmarked} * {call} = {unmarked * call}")


def bingo_1(test = False):
    calls, boards = load_data(test)
    for call in calls:
        mark_call(call, boards)
        for board in boards:
            if test_won(board):
                print_winner(call, board)
                return


def bingo_2(test = False):
    calls, boards = load_data(test)
    for call in calls:
        mark_call(call, boards)
        losers = [board for board in boards if not test_won(board)]
        if len(boards) == 1 and not losers:
            print_winner(call, boards[0])
            return

        boards = losers


def run():
    bingo_1(True)
    bingo_1()
    bingo_2(True)
    bingo_2()


if __name__ == "__main__":
    run()
