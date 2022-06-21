#! /usr/bin/python

from typing import List, Tuple, Dict
from get_input import get_input_for_day
from collections import Counter


ZERO = 'abcefg'
ONE = 'cf'
TWO = 'acdeg'
THREE = 'acdfg'
FOUR = 'bcdf'
FIVE = 'abdfg'
SIX = 'abdefg'
SEVEN = 'acf'
EIGHT = 'abcdefg'
NINE = 'abcdfg'


def parse_input(input_data: List[str]) -> Tuple[List[str], List[str]]:
    signal_patterns = []
    output_values = []
    for line in input_data:
        signal_patterns += line.split('|')[0][:-1].split(' ')
        output_values += line.split('|')[1][1:].split(' ')
    return signal_patterns, output_values


def part_one(output_values: List[str]) -> int:
    digit_count = 0
    for value in output_values:
        if len(value) == len(ONE) or len(value) == len(FOUR) or len(value) == len(SEVEN) or len(value) == len(EIGHT):
            digit_count += 1
    return digit_count


def get_count_of_all_letters(signal_pattern: List[str]) -> Dict[str, int]:
    all_letters = ''.join(signal_pattern)
    letter_counts = Counter(all_letters)
    return letter_counts


def find_a_value(one_pattern: str, seven_pattern: str) -> str:
    a_value = seven_pattern.replace(one_pattern[0], '').replace(one_pattern[1], '')
    return a_value


def find_bef_values(letter_counts: Dict[str, int]) -> Tuple[str, str, str]:
    for letter, count in letter_counts.items():
        if count == 4:
            e_value = letter
        if count == 6:
            b_value = letter
        if count == 9:
            f_value = letter
    return b_value, e_value, f_value


def find_c_value(one_pattern: str, f_value: str) -> str:
    return one_pattern.replace(f_value, '')


def find_d_value(four_pattern: str, b_value: str, c_value: str, f_value: str) -> str:
    return four_pattern.replace(b_value, '').replace(c_value, '').replace(f_value, '')


def find_g_value(eight_pattern: str, all_values: List[str]) -> str:
    for letter in eight_pattern:
        if letter in all_values:
            continue
        return letter


def translate_letters(all_values:  List[str], output_values: List[str]) -> List[str]:
    translation_map = {}
    translation_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for index in range(0, len(all_values)):
        translation_map[all_values[index]] = translation_list[index]
    translated_output_values = []
    for value in output_values:
        translated_value = ''
        for letter in value:
            translated_value += translation_map[letter]
        translated_output_values.append(''.join(sorted(translated_value)))
    return translated_output_values


def get_number_from_values(translated_values: List[str]) -> int:
    values = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
    output_value_sum = ''
    for value in translated_values:
        output_value_sum += str(values.index(value))
    return int(output_value_sum)


def part_two(input_data: List[str]) -> int:
    total_sum = 0
    for line in input_data:
        signal_pattern = sorted(line.split('|')[0][:-1].split(' '), key=len)
        output_values = line.split('|')[1][1:].split(' ')
        letter_counts = get_count_of_all_letters(signal_pattern)

        one_pattern = signal_pattern[0]
        seven_pattern = signal_pattern[1]
        four_pattern = signal_pattern[2]
        eight_pattern = signal_pattern[-1]
        a_value = find_a_value(one_pattern, seven_pattern)
        b_value, e_value, f_value = find_bef_values(letter_counts)

        c_value = find_c_value(one_pattern, f_value)
        d_value = find_d_value(four_pattern, b_value, c_value, f_value)

        all_values = [a_value,b_value,c_value,d_value,e_value,f_value]
        g_value = find_g_value(eight_pattern, all_values)
        all_values.append(g_value)

        translated_values = translate_letters(all_values, output_values)

        total_sum += get_number_from_values(translated_values)

    return total_sum


if __name__ == "__main__":
    input_data = [x.decode() for x in get_input_for_day(8)]
    signal_patterns, output_values = parse_input(input_data)
    part_one_answer = part_one(output_values)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
