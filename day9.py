#! /usr/bin/python

from typing import List, Tuple
from get_input import get_input_for_day

Coord = Tuple[int, int]


def find_adjacent_coords(x: int, y: int, max_x_coord: int, max_y_coord: int) -> List[Coord]:
    coords = []
    if x:
        coords.append((x-1, y))
    if x < max_x_coord:
        coords.append((x+1, y))
    if y:
        coords.append((x, y-1))
    if y < max_y_coord:
        coords.append((x, y+1))

    return coords


def calculate_risk_level(minimums: List[str]) -> int:
    risk_level = 0
    for minimum in minimums:
        risk_level += int(minimum) + 1
    return risk_level


def part_one(input_data: List[str]) -> int:
    minimums = []
    max_y_coord = len(input_data) - 1
    max_x_coord = len(input_data[0]) - 1
    for y in range(0, len(input_data)):
        for x in range(0, len(input_data[y])):
            current_height = input_data[y][x]
            adj_coords = find_adjacent_coords(x, y, max_x_coord, max_y_coord)
            potential_mins = []
            for (adj_x, adj_y) in adj_coords:
                potential_mins += [input_data[adj_y][adj_x]]
            if current_height < min(potential_mins) and current_height not in potential_mins:
                minimums.append(current_height)

    return calculate_risk_level(minimums)


def define_base_case(x: int, y: int, max_x_coord: int, max_y_coord: int) -> bool:
    if x < 0:
        return True
    if y < 0:
        return True
    if x > max_x_coord:
        return True
    if y > max_y_coord:
        return True


def find_basin(starting_point: Coord, max_x_coord: int, max_y_coord: int, input_data: List[str], visited: List[Coord] = [], basin_count: int = 0) -> int:
    x = starting_point[0]
    y = starting_point[1]
    if define_base_case(x, y, max_x_coord, max_y_coord):
        print('hit base case')
        return 0
    if starting_point in visited:
        return 0
    visited.append(starting_point)

    height = input_data[y][x]
    if height == '9':
        return 0
    basin_count += 1
    basin_count += find_basin((x+1, y), max_x_coord, max_y_coord, input_data, visited)
    basin_count += find_basin((x-1, y), max_x_coord, max_y_coord, input_data, visited)
    basin_count += find_basin((x, y+1), max_x_coord, max_y_coord, input_data, visited)
    basin_count += find_basin((x, y-1), max_x_coord, max_y_coord, input_data, visited)

    return basin_count


def part_two(input_data: List[str]) -> int:
    minimums = []
    max_y_coord = len(input_data) - 1
    max_x_coord = len(input_data[0]) - 1
    for y in range(0, len(input_data)):
        for x in range(0, len(input_data[y])):
            current_height = input_data[y][x]
            adj_coords = find_adjacent_coords(x, y, max_x_coord, max_y_coord)
            potential_mins = []
            for (adj_x, adj_y) in adj_coords:
                potential_mins += [input_data[adj_y][adj_x]]
            if current_height < min(potential_mins) and current_height not in potential_mins:
                minimums.append((x, y))

    basins = []
    for coord in minimums:
        basins.append(find_basin(coord, max_x_coord, max_y_coord, input_data))

    basins.sort(reverse=True)

    return basins[0] * basins[1] * basins[2]


if __name__ == "__main__":
    test_data = [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]
    input_data = [x.decode() for x in get_input_for_day(9)]

    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
