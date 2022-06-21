#! /usr/bin/python3

from typing import List
from get_input import get_input_for_day


def part_one(input_data: List[str]) -> int:
    final_coordinates = [0,0]
    for direction in input_data:
        distance = int(direction.split(' ')[1])
        if 'forward' in direction:
            final_coordinates[0] += distance
        elif 'down' in direction:
            final_coordinates[1] += distance
        elif 'up' in direction:
            final_coordinates[1] -= distance

    return final_coordinates[0] * final_coordinates[1]


def part_two(input_data: List[str]) -> int:
    final_coordinates = [0, 0]
    aim = 0
    for direction in input_data:
        distance = int(direction.split(' ')[1])
        if 'forward' in direction:
            final_coordinates[0] += distance
            final_coordinates[1] += aim * distance
        elif 'down' in direction:
            aim += distance
        elif 'up' in direction:
            aim -= distance
    return final_coordinates[0] * final_coordinates[1]


if __name__ == "__main__":
    input_data = [x.decode() for x in get_input_for_day(2)]
    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
