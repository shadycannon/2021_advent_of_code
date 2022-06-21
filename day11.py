#! /usr/bin/python

from typing import List, Tuple
from get_input import get_input_for_day
Coord = Tuple[int, int]


class SquidSimulation:
    def __init__(self, input_data: List[str], steps: int) -> None:
        self.current = (0, 0)
        self.steps = steps
        self.num_flashes = 0
        squids = []
        for y in range(0, len(input_data)):
            squids.append([int(x) for x in input_data[y]])
        self.squids = squids

    def squid_gen(self) -> Tuple[int, int]:
        squids = self.squids
        for y in range(0, len(squids)):
            for x in range(0, len(squids[y])):
                yield x, y

    def print_squids(self, desired_output: List[List] = []) -> None:
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

    def flash_tens(self) -> bool:
        all_xs = True
        squids = self.squids
        for (x, y) in self.squid_gen():
            if squids[y][x] == 'x':
                squids[y][x] = 0
            else:
                all_xs = False
        return all_xs

    def increase_energy(self) -> None:
        squids = self.squids
        for y in range(0, len(squids)):
            for x in range(0, len(squids[y])):
                squids[y][x] += 1

    def determine_adj_squids(self, squid: Coord) -> List[Coord]:
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

    def flash_explosion(self, flashed_squid: Coord, adj_squids: List[Coord]) -> None:
        squids = self.squids
        squids[flashed_squid[1]][flashed_squid[0]] = 'x'
        self.num_flashes += 1
        for x, y in adj_squids:
            if squids[y][x] != 'x':
                squids[y][x] += 1
                if squids[y][x] >= 10:
                    self.flash_explosion((x, y), self.determine_adj_squids((x, y)))

    def part_one(self) -> None:
        squids = self.squids
        for step in range(0, self.steps):
            self.increase_energy()
            for x, y in self.squid_gen():
                if squids[y][x] != 'x' and squids[y][x] >= 10:
                    adj_squids = self.determine_adj_squids((x, y))
                    self.flash_explosion((x, y), adj_squids)
            self.flash_tens()

    def part_two(self) -> int:
        squids = self.squids
        for step in range(0, self.steps):
            self.increase_energy()
            for x, y in self.squid_gen():
                if squids[y][x] != 'x' and squids[y][x] >= 10:
                    adj_squids = self.determine_adj_squids((x, y))
                    self.flash_explosion((x, y), adj_squids)
            all_flashed = self.flash_tens()
            if all_flashed:
                return step + 1


if __name__ == "__main__":
    test_data = [
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

    s.part_one()
    print(s.num_flashes)
    print(s.part_two())

