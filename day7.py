#! /usr/bin/python
import sys
from typing import List
from get_input import get_input_for_day

DAYS = 256
REPRODUCTION_TIME = 7


def part_one(input_data: List[str]) -> int:
    crabs = sorted([int(x) for x in input_data[0].split(',')])
    min_fuel_used = sys.maxsize
    for horiz_position in range(crabs[0], crabs[-1] + 1):
        fuel_used = 0
        for crab in crabs:
            fuel_used += abs(crab-horiz_position)
        if fuel_used < min_fuel_used:
            min_fuel_used = fuel_used

    return min_fuel_used


def calculate_fuel_usage(movement: int) -> int:
    fuel = int(((1 + movement) * movement) / 2)
    return fuel


def part_two(input_data: List[str]) -> int:
    crabs = sorted([int(x) for x in input_data[0].split(',')])
    min_fuel_used = None
    for horiz_position in range(crabs[0], crabs[-1] + 1):
        fuel_used = 0
        for crab in crabs:
            fuel_used += calculate_fuel_usage(abs(crab-horiz_position))
        if not min_fuel_used or fuel_used < min_fuel_used:
            min_fuel_used = fuel_used

    return min_fuel_used


if __name__ == "__main__":
    test_data = ["16,1,2,0,4,2,7,1,2,14"]
    input_data = [x.decode() for x in get_input_for_day(7)]
    print(calculate_fuel_usage(4))
    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
