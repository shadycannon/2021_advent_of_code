#! /usr/bin/python

from typing import List, Tuple
from get_input import get_input_for_day


class PaperFolder:
    def __init__(self, input_data: List[str]) -> None:
        folding = False
        coords = []
        max_x = 0
        max_y = 0
        folding_instructions = []
        for line in input_data:
            if not line.strip():
                folding = True
                continue
            if folding:
                folding_instructions.append(line.split(' ')[2].split('='))
            else:
                x, y = line.split(',')
                x = int(x)
                y = int(y)
                coords.append((x, y))

                max_x = max(max_x, x)
                max_y = max(max_y, y)

        self.folding_instructions = folding_instructions
        self.coords = coords
        self.max_coords = [max_x, max_y]
        self.max_x = max_x
        self.max_y = max_y

    def split_grid(self, folding_instruction: List[str]) -> Tuple[List[list], List[list]]:
        grid1 = []
        grid2 = []
        axis = 0 if folding_instruction[0] == 'x' else 1
        value = int(folding_instruction[1])
        for coord in self.coords:
            if coord[axis] < value:
                grid1.append(coord)
            elif coord[axis] > value:
                grid2.append(coord)

        grid1 = [list(x) for x in grid1]
        grid2 = [list(x) for x in grid2]

        self.transform_smaller_grid(grid1, grid2, axis, value)

        grid1 = [tuple(x) for x in grid1]
        grid2 = [tuple(x) for x in grid2]


        return grid1, grid2

    def transform_smaller_grid(self, grid1: List[list], grid2: List[list], axis: int, value: int) -> None:
        max_value = self.max_coords[axis]
        if value < max_value / 2:
            smaller_grid = grid1
        else:
            smaller_grid = grid2

        for i in range(0, len(smaller_grid)):
            smaller_grid[i][axis] = 2 * value - smaller_grid[i][axis]

        self.max_coords[axis] = value - 1

    def part_one(self) -> None:
        folding_instruction = self.folding_instructions[0]
        grid1, grid2 = self.split_grid(folding_instruction)

        self.coords = set(grid1 + grid2)

    def print_grid(self) -> None:
        for y in range(0, self.max_coords[1] + 1):
            row = ''
            for x in range(0, self.max_coords[0] + 1):
                if (x,y) in self.coords:
                    row += '#'
                else:
                    row += '.'
            print(row)

    def part_two(self) -> None:
        for instruction in self.folding_instructions:

            grid1, grid2 = self.split_grid(instruction)

            self.coords = list(set(grid1 + grid2))


if __name__ == "__main__":
    test_data = [
        '6,10',
        '0,14',
        '9,10',
        '0,3',
        '10,4',
        '4,11',
        '6,0',
        '6,12',
        '4,1',
        '0,13',
        '10,12',
        '3,4',
        '3,0',
        '8,4',
        '1,10',
        '2,14',
        '8,10',
        '9,0',
        '\n',
        'fold along y=7',
        'fold along x=5',
    ]
    input_data = [x.decode() for x in get_input_for_day(13)]

    pf = PaperFolder(input_data)
    print(pf.part_two())
    pf.print_grid()
    print(pf.part_one())
    pf.print_grid()

