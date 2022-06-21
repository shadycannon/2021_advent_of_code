#! /usr/bin/python

from typing import List
from get_input import get_input_for_day
from collections import Counter, defaultdict


def part_one(input_data: List[str]) -> int:
    columns = defaultdict(str)
    for row in input_data:
        for i in range(0, len(row)):
            columns[i] += row[i]

    gamma_number = ''.join([Counter(x).most_common()[0][0] for x in columns.values()])
    epsilon_number = ''.join([Counter(x).most_common()[1][0] for x in columns.values()])

    gamma_number_dec = int(gamma_number, 2)
    epsilon_number_dec = int(epsilon_number, 2)

    return gamma_number_dec * epsilon_number_dec


def part_two(input_data: List[str]) -> int:
    columns = defaultdict(str)
    for row in input_data:
        for i in range(0, len(row)):
            columns[i] += row[i]
    good_oxygen_numbers = input_data
    good_co2_numbers = input_data
    oxygen_decimal = 0
    co2_decimal = 0
    for index in range(0, len(input_data[0])):
        ox_column = [x[index] for x in good_oxygen_numbers]
        co2_column = [x[index] for x in good_co2_numbers]
        new_good_oxygen_numbers = []
        new_good_co2_numbers = []
        ox_column_counter = Counter(ox_column).most_common()
        co2_column_counter = Counter(co2_column).most_common()

        if len(ox_column_counter) < 2:
            most_common_bit = ox_column_counter[0][0]
        elif ox_column_counter[0][1] == ox_column_counter[1][1]:
            most_common_bit = '1'
        else:
            most_common_bit = ox_column_counter[0][0]
        for number in good_oxygen_numbers:
            if number[index] == most_common_bit:
                new_good_oxygen_numbers.append(number)
        good_oxygen_numbers = new_good_oxygen_numbers
        if len(good_oxygen_numbers) == 1:
            oxygen_decimal = int(good_oxygen_numbers[0], 2)

        if len(co2_column_counter) < 2:
            least_common_bit = co2_column_counter[0][0]
        elif co2_column_counter[0][1] == co2_column_counter[1][1]:
            least_common_bit = '0'
        else:
            least_common_bit = co2_column_counter[1][0]
        for number in good_co2_numbers:
            if number[index] == least_common_bit:
                new_good_co2_numbers.append(number)
        good_co2_numbers = new_good_co2_numbers
        if len(good_co2_numbers) == 1:
            co2_decimal = int(good_co2_numbers[0], 2)

    return oxygen_decimal * co2_decimal


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
    input_data = [x.decode() for x in get_input_for_day(3)]

    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
