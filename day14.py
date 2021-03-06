#! /usr/bin/python

from typing import List, Dict
from get_input import get_input_for_day
from collections import defaultdict,Counter

class Polymers:
    def __init__(self, input_data: List[str], steps: int) -> None:
        self.steps = steps
        self.rules = {}
        self.template = input_data[0]
        for line in input_data[2:]:
            pair, insertion = line.split(' -> ')
            self.rules[pair] = insertion

        self.template_counts = self.get_template_counts()
        print(f'init: {self.template_counts}')

    def get_template_counts(self) -> Dict[str, int]:
        pair_counts = defaultdict(int)
        for i in range(0, len(self.template) - 1):
            polymer_pair = self.template[i] + self.template[i+1]
            pair_counts[polymer_pair] += 1
        return pair_counts

    def insert_polymer(self) -> str:
        new_template = self.template[0]
        for i in range(0, len(self.template) -1):
            polymer_pair = self.template[i] + self.template[i+1]
            new_template += self.rules[polymer_pair] + polymer_pair[1]
        return new_template

    def part_one(self) -> int:
        for i in range(0, self.steps):
            self.template = self.insert_polymer()
        counter = Counter(self.template).most_common()
        return counter[0][1] - counter[-1][1]

    def insert_polymer_counts(self) -> Dict[str, int]:
        new_template_counts = defaultdict(int)
        for pair in self.template_counts:
            pair_count = self.template_counts[pair]
            insertion_letter = self.rules[pair]
            new_pair1 = pair[0] + insertion_letter
            new_pair2 = insertion_letter + pair[1]
            new_template_counts[new_pair1] += pair_count
            new_template_counts[new_pair2] += pair_count

        return new_template_counts

    def count_letters_from_pairs(self) -> Dict[str, int]:
        letter_counts = defaultdict(int)
        for pair in self.template_counts:
            letter_counts[pair[0]] += self.template_counts[pair]
            letter_counts[pair[1]] += self.template_counts[pair]
        for letter, count in letter_counts.items():
            if letter == self.template[0] or letter == self.template[-1]:
                letter_counts[letter] = (letter_counts[letter] + 1)/2
            else:
                letter_counts[letter] /= 2
        return letter_counts

    def part_two(self) -> int:
        for i in range(0, self.steps):
            self.template_counts = self.insert_polymer_counts()

        letter_counts = self.count_letters_from_pairs()
        ordered_counts = sorted(list(letter_counts.values()))

        return int(ordered_counts[-1] - ordered_counts[0])


if __name__ == "__main__":
    test_data = [
        'NNCB',
        '\n',
        'CH -> B',
        'HH -> N',
        'CB -> H',
        'NH -> C',
        'HB -> C',
        'HC -> B',
        'HN -> C',
        'NN -> C',
        'BH -> H',
        'NC -> B',
        'NB -> B',
        'BN -> B',
        'BB -> N',
        'BC -> B',
        'CC -> N',
        'CN -> C',
    ]
    input_data = [x.decode() for x in get_input_for_day(14)]
    p = Polymers(input_data, 40)
    print(p.part_one())
    print(p.part_two())


