#! /usr/bin/python

from get_input import get_input_for_day
from itertools import permutations

from collections import defaultdict,Counter
from statistics import median


class SquidSimulation:
    def __init__(self, input_data, steps):
        self.current = (0, 0)
        self.steps = steps
        self.num_flashes = 0
        squids = []
        for y in range(0, len(input_data)):
            squids.append([int(x) for x in input_data[y]])
        self.squids = squids

    def squid_gen(self):
        squids = self.squids
        for y in range(0, len(squids)):
            for x in range(0, len(squids[y])):
                yield x, y

    def print_squids(self, desired_output=[]):
        squids = self.squids
        print('-' * (len(squids[0]) * 2 - 1))
        for y in range(0, len(squids)):
            row = ''
            for x in range(0, len(squids[y])):
                row += str(squids[y][x]) + ' '
            if desired_output:
                row += '   '
                for x in range(0, len(squids[y])):
                    row += str(desired_output[y][x]) + ' '
            print(row)

        print('-' * (len(squids[0]) * 2 - 1))

    def flash_tens(self):
        all_xs = True
        squids = self.squids
        for (x, y) in self.squid_gen():
            if squids[y][x] == 'x':
                squids[y][x] = 0
            else:
                all_xs = False
        return all_xs

    def increase_energy(self):
        squids = self.squids
        for y in range(0, len(squids)):
            for x in range(0, len(squids[y])):
                squids[y][x] += 1

    def determine_adj_squids(self, squid):
        squids = self.squids
        adj_squids = []
        squid_x = squid[0]
        squid_y = squid[1]
        for x in range(-1, 2):
            new_x = squid_x + x
            if 0 <= new_x < len(squids[0]):
                for y in range(-1, 2):
                    new_y = squid_y + y
                    if 0 <= new_y < len(squids):
                        if not (new_y == squid_y and new_x == squid_x):
                            adj_squids.append((new_x, new_y))

        return adj_squids

    def flash_explosion(self, flashed_squid, adj_squids):
        squids = self.squids
        squids[flashed_squid[1]][flashed_squid[0]] = 'x'
        self.num_flashes += 1
        for x, y in adj_squids:
            if squids[y][x] != 'x':
                squids[y][x] += 1
                if squids[y][x] >= 10:
                    self.flash_explosion((x, y), self.determine_adj_squids((x, y)))

    def part_one(self):
        squids = self.squids
        for step in range(0, self.steps):
            self.increase_energy()
            for x, y in self.squid_gen():
                if squids[y][x] != 'x' and squids[y][x] >= 10:
                    adj_squids = self.determine_adj_squids((x, y))
                    self.flash_explosion((x, y), adj_squids)
            self.flash_tens()


    def part_two(self):
        squids = self.squids
        for step in range(0, self.steps):
            self.increase_energy()
            for x, y in self.squid_gen():
                if squids[y][x] != 'x' and squids[y][x] >= 10:
                    adj_squids = self.determine_adj_squids((x, y))
                    self.flash_explosion((x, y), adj_squids)
            all_flashed = self.flash_tens()
            if all_flashed:
                print("sdfklh")
                return step + 1
            self.print_squids()


if __name__ == "__main__":
    input_data = [
        '5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526',
    ]
    input_data = [x.decode() for x in get_input_for_day(11)]

    s = SquidSimulation(input_data, 1000)

    #print(s.part_one())
    #print(s.num_flashes)
    print(s.part_two())
    #part_one_answer = part_one(input_data)
    #part_two_answer = part_two(input_data)
    #print(f'part_one_answer: {part_one_answer}')
    #print(f'part_two_answer: {part_two_answer}')
