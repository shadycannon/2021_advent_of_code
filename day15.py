#!/usr/bin/python3

from get_input import get_input_for_day
import sys

from collections import defaultdict, OrderedDict


class CaveTraverse:
    def __init__(self, input_data: list):
        self.lowest_total_risk = None
        chiton_grid = []
        for y in range(0, len(input_data)):
            chiton_grid.append([])
            row = input_data[y]
            for x in range(0, len(row)):
                chiton_grid[y].append(int(row[x]))

        self.chiton_grid = chiton_grid
        self.max_y = len(chiton_grid)
        self.max_x = len(chiton_grid[0])
        self.swap_first = False

        left_column = [row[0] for row in chiton_grid]
        right_column = [row[-1] for row in chiton_grid]
        self.potential_min_rd = sum(chiton_grid[0]) + sum(right_column)
        self.potential_min_dr = sum(chiton_grid[-1]) + sum(left_column)
        self.lowest_total_risk = min(self.potential_min_dr, self.potential_min_rd)
        self.all_nodes = [(x,y) for y in range(0,len(chiton_grid)) for x in range(0, len(chiton_grid[y]))]

    def get_hueristic_value(self, coord: tuple) -> int:
        return abs(self.max_x - coord[0]) + abs(self.max_y - coord[1]) + self.get_risk_value(coord) * 2

    def find_next_steps(self, starting_coord: tuple, previous_steps: list) -> list:
        new_coords_info = defaultdict(int)
        (x, y) = starting_coord

        for addition in [-1, 1]:
            new_x = x + addition
            new_y = y + addition

            if 0 <= new_x + addition <= self.max_x:
                new_coord = (new_x, y)
                if new_coord not in previous_steps:
                    new_coords_info[new_coord] = self.get_hueristic_value(new_coord)

            if 0 <= new_y + addition <= self.max_y:
                new_coord = (x, new_y)
                if new_coord not in previous_steps:
                    new_coords_info[new_coord] = self.get_hueristic_value(new_coord)

        ordered_coords = OrderedDict(sorted(new_coords_info.items(), key=lambda t: t[1]))
        return list(ordered_coords.keys())

    def find_neighbors(self, starting_coord: list, unvisited_node: list) -> list:
        new_coords_info = defaultdict(int)
        (x, y) = starting_coord

        for addition in [-1, 1]:
            new_x = x + addition
            new_y = y + addition

            if 0 <= new_x + addition <= self.max_x:
                new_coord = (new_x, y)
                if new_coord in unvisited_node:
                    new_coords_info[new_coord] = self.get_hueristic_value(new_coord)

            if 0 <= new_y + addition <= self.max_y:
                new_coord = (x, new_y)
                if new_coord in unvisited_node:
                    new_coords_info[new_coord] = self.get_hueristic_value(new_coord)

        ordered_coords = OrderedDict(sorted(new_coords_info.items(), key=lambda t: t[1]))

        return list(ordered_coords.keys())

    def get_risk_value(self, coord: tuple) -> int:
        return self.chiton_grid[coord[1]][coord[0]]

    def find_all_paths(self, starting_point: tuple = (0, 0), previous_steps: list = [], total_risk: int = 0) -> None:
        new_previous_steps = previous_steps[:]
        new_previous_steps.append(starting_point)
        if total_risk > self.lowest_total_risk:
            return
        if starting_point == (self.max_x - 1, self.max_y - 1):
            self.lowest_total_risk = min(total_risk, self.lowest_total_risk)
            return
        next_steps = self.find_next_steps(starting_point, new_previous_steps)
        for step in next_steps:
            risk = self.get_risk_value(step)
            self.find_all_paths(step, new_previous_steps, total_risk + risk)

    def print_grid(self, chiton_grid: list = None):
        if not chiton_grid:
            chiton_grid = self.chiton_grid
        for y in range(0, len(chiton_grid)):
            row = chiton_grid[y]
            print(''.join([str(x) for x in row]))

    def dijkstra_algorithm(self):
        max_value = sys.maxsize
        start_node = (0, 0)
        shortest_path = {}
        unvisited_nodes = self.all_nodes
        previous_nodes = {}
        target_node = (self.max_x -1, self.max_y -1)
        for node in unvisited_nodes:
            shortest_path[node] = max_value

        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if not current_min_node:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
            neighbors = self.find_neighbors(current_min_node, unvisited_nodes)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.get_risk_value(neighbor)

                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        path.append(start_node)
        print(f"best path: {shortest_path[target_node]}")

    def part_one(self) -> int:
        self.find_all_paths()
        return self.lowest_total_risk

    def get_new_value(self, value, distance):
        new_value = value + distance
        if new_value > 9:
            new_value = new_value % 10 + 1
        return new_value

    def expand_map(self) -> list:
        expansion_factor = 5
        chiton_grid = self.chiton_grid

        new_row = ['.' for _ in range(0, self.max_x * expansion_factor)]
        new_grid = {l: new_row[:] for l in range(0, self.max_y * expansion_factor)}

        for i in range(0, 5):
            for j in range(0, 5):
                for y in range(0, len(chiton_grid)):
                    for x in range(0, len(chiton_grid[0])):

                        index_y = i * self.max_y + y
                        index_x = j * self.max_x + x
                        new_grid[index_y][index_x] = self.get_new_value(chiton_grid[y][x], i+j)

        self.chiton_grid = new_grid
        self.max_y = len(self.chiton_grid)
        self.max_x = len(self.chiton_grid[0])
        self.all_nodes = [(x,y) for y in range(0,len(self.chiton_grid)) for x in range(0, len(self.chiton_grid[y]))]

        return new_grid


if __name__ == "__main__":
    test_data = [
        '1163751742',
        '1381373672',
        '2136511328',
        '3694931569',
        '7463417111',
        '1319128137',
        '1359912421',
        '3125421639',
        '1293138521',
        '2311944581',
    ]
    input_data = [x.decode() for x in get_input_for_day(15)]

    c = CaveTraverse(input_data)
    c.expand_map()
    c.print_grid()
    c.dijkstra_algorithm()

