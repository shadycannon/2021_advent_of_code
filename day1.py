#! /usr/bin/python3

import sys
from typing import List
from get_input import get_input_for_day


def part_one(input_data: List[int]) -> int:
    previous_distance = sys.maxsize
    larger_distance_count = 0
    for distance in input_data:
        if distance > previous_distance:
            larger_distance_count += 1
        previous_distance = distance
    return larger_distance_count


def part_two(input_data: List[int]) -> int:
    larger_sum_count = 0
    previous_sum = input_data[0] + input_data[1] + input_data[2]
    for i in range(3, len(input_data)):
        distance_sum = input_data[i] + input_data[i-1] + input_data[i-2]
        if distance_sum > previous_sum:
            larger_sum_count += 1
        previous_sum = distance_sum
    return larger_sum_count


if __name__ == "__main__":
    input_data = [int(x) for x in get_input_for_day(1)]
    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
