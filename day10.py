#! /usr/bin/python

from get_input import get_input_for_day
from collections import defaultdict,Counter
from statistics import median


LEFT_CHARACTERS = ['[', '(', '{', '<']
RIGHT_CHARACTERS = [']', ')', '}', '>']


def is_matching(char1, char2):
    for index in range(len(LEFT_CHARACTERS)):
        if char1 == LEFT_CHARACTERS[index] and char2 == RIGHT_CHARACTERS[index]:
            return True
        if char2 == LEFT_CHARACTERS[index] and char1 == RIGHT_CHARACTERS[index]:
            return True

    return False


def get_illegal_character(syntax_line):
    stack = []
    for character in syntax_line:
        if stack:
            if character in RIGHT_CHARACTERS and not is_matching(character, stack[-1]):
                return character
            elif is_matching(character, stack[-1]):
                stack.pop()
                continue
        stack.append(character)


def get_incomplete_characters(syntax_line):
    stack = []
    for character in syntax_line:
        if stack:
            if character in RIGHT_CHARACTERS and not is_matching(character, stack[-1]):
                return False
            elif is_matching(character, stack[-1]):
                stack.pop()
                continue
        stack.append(character)
    return stack

def score_illegal_character(character):
    scoring_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return scoring_map[character]


def part_one(input_data):
    score = 0
    for line in input_data:
        illegal_character = get_illegal_character(line)
        if illegal_character:
            score += score_illegal_character(illegal_character)
    return score


def complete_characters(incomplete_characters):
    matching_map = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>',
    }
    matching_characters = []
    for index in range(len(incomplete_characters) -1, -1, -1):
        matching_characters.append(matching_map[incomplete_characters[index]])
    return matching_characters


def score_complete_characters(complete_characters):
    scoring_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for character in complete_characters:
        score *= 5
        score += scoring_map[character]
    return score


def part_two(input_data):
    all_scores = []
    for line in input_data:
        incomplete_characters = get_incomplete_characters(line)
        if incomplete_characters:
            all_scores.append(score_complete_characters(complete_characters(incomplete_characters)))

    return median(all_scores)


if __name__ == "__main__":
    input_data = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]
    input_data = [x.decode() for x in get_input_for_day(10)]

    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
