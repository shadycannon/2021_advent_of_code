#! /usr/bin/python

from get_input import get_input_for_day
from itertools import permutations

from collections import defaultdict,Counter
from statistics import median

class PaperFolderWithGrid:
    def __init__(self, input_data):
        folding = False
        self.folding_instructions = []
        coords = []
        max_x = 0
        max_y = 0
        for line in input_data:
            if not line.strip():
                folding = True
                continue
            if folding:
                self.folding_instructions.append(line.split(' ')[2].split('='))
            else:
                x,y = line.split(',')
                x= int(x)
                y = int(y)
                coords.append((x,y))

                max_x = max(max_x, x)
                max_y = max(max_y, y)


        self.grid = []
        for y in range(0, max_y + 1):
            self.grid.append([])
            for x in range(0, max_x + 1):
                if (x,y) in coords:
                    self.grid[y].append('#')
                else:
                    self.grid[y].append('.')


    def gen_grid_loop(self, grid=None):
        if not grid:
            grid = self.grid
        for y in range(0, len(grid)):
            for x in range(0, len(grid[0])):
                yield x,y


    def print_grid(self, grid=None):
        if not grid:
            grid = self.grid
        row = ''
        for x,y in self.gen_grid_loop(grid):
            row += grid[y][x]
            if len(row) == len(grid[0]):
                print(row)
                row = ''

    def split_grids(self, line):
        grid1 = []
        grid2 = []
        value = int(line[1])
        if line[0] == 'x':
            for y in range(0, len(self.grid)):
                first_half = self.grid[y][:value]
                second_half = self.grid[y][value+1:]
                second_half.reverse()
                grid1.append(first_half)
                grid2.append(second_half)

        else:
            grid1 = self.grid[:value]
            grid2 = self.grid[:value+1]
            grid2.reverse()

        return grid1, grid2

    def overlap_grids(self, grid1, grid2):
        grid1_area = len(grid1) * len(grid1[0])
        grid2_area = len(grid2) * len( )

        for x,y in self.gen_grid_loop(grid1):
            if grid2[y][x] == '#':
                grid1[y][x] = '#'

        return grid1


    def count_dots(self):
        c = Counter([x for y in self.grid for x in y])
        return c['#']

    def part_one_with_grid(self):
        folding_instruction = self.folding_instructions[1]
        grid1, grid2 = self.split_grids(folding_instruction)
        print('grid1')

        self.print_grid(grid1)
        print('grid2')

        self.print_grid(grid2)
        print('wtf')

        #new_grid = self.overlap_grids(grid1, grid2)
        #self.grid = new_grid
        #return self.count_dots()



class PaperFolder:
    def __init__(self, input_data):
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

    def split_grid(self, folding_instruction):
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

    def transform_smaller_grid(self, grid1, grid2, axis, value):
        max_value = self.max_coords[axis]
        if value < max_value / 2:
            smaller_grid = grid1
        else:
            smaller_grid = grid2

        for i in range(0, len(smaller_grid)):
            smaller_grid[i][axis] = 2 * value - smaller_grid[i][axis]

        self.max_coords[axis] = value - 1


    def part_one(self):
        folding_instruction = self.folding_instructions[0]
        grid1, grid2 = self.split_grid(folding_instruction)

        self.coords = set(grid1 + grid2)

    def print_grid(self):
        for y in range(0, self.max_coords[1] + 1):
            row = ''
            for x in range(0, self.max_coords[0] + 1):
                if (x,y) in self.coords:
                    row += '#'
                else:
                    row += '.'
            print(row)



    def part_two(self):
        for instruction in self.folding_instructions:

            grid1, grid2 = self.split_grid(instruction)

            self.coords = list(set(grid1 + grid2))


if __name__ == "__main__":
    input_data = [
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
    #print(pf.part_one())
    #print(pf.part_two())
    #print(s.part_one())
    #print(s.num_flashes)
    #part_one_answer = part_one(input_data)
    #part_two_answer = part_two(input_data)
    #print(f'part_one_answer: {part_one_answer}')
    #print(f'part_two_answer: {part_two_answer}')
