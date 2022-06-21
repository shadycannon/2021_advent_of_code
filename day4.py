#! /usr/bin/python

from typing import List, Tuple, Dict
from get_input import get_input_for_day
from collections import defaultdict


def check_for_bingo(board: List[str]) -> bool:
    columns = defaultdict(list)
    for row in board:
        if ''.join(row) == 'x'*len(row):
            return True
        for i in range(0, len(row)):
            columns[i].append(row[i])

    for column in columns.values():
        if ''.join(column) == 'x'*len(column):
            return True

    return False


def mark_board(number: str, board: List[str]) -> None:
    for row in board:
        for value in row:
            if number == value:
                row[row.index(number)] = 'x'


def get_score(number: str, board: List[str]) -> int:
    sum = 0
    for row in board:
        for value in row:
            if value != 'x':
                sum += int(value)
    return sum * int(number)


def part_one(numbers_called: List[str], boards: Dict[List]) -> int:
    for number in numbers_called:
        for board in boards.values():
            mark_board(number, board)
            if check_for_bingo(board):
                return get_score(number, board)


def part_two(numbers_called: List[str], boards_dict: Dict[List]) -> int:
    boards = boards_dict.values()
    losing_boards = boards
    for number in numbers_called:
        new_losing_boards = []
        for board in losing_boards:
            mark_board(number, board)
            if not check_for_bingo(board):
                new_losing_boards.append(board)
        if not new_losing_boards:
            return get_score(number, losing_boards[0])
        losing_boards = new_losing_boards


def process_input(input_data: List[str]) -> Tuple[List[str], Dict[List]]:
    numbers_called = input_data[0].split(',')
    boards = defaultdict(list)
    board_count = -1
    for row in input_data[1:]:
        if not row:
            board_count += 1
            continue
        row_list = row.split(' ')
        boards[board_count].append([x for x in row_list if x])
    return numbers_called, boards


if __name__ == "__main__":
    test_data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
    ]
    input_data = [x.decode() for x in get_input_for_day(4)]
    numbers_called, boards = process_input(input_data)

    part_one_answer = part_one(numbers_called, boards)
    part_two_answer = part_two(numbers_called, boards)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')

