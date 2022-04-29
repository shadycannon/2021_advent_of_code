#! /usr/bin/python

from get_input import get_input_for_day
from collections import defaultdict


def process_coords_diags(coord):
    point1 = coord.split('->')[0].strip()
    point2 = coord.split('->')[1].strip()
    point1_x = int(point1.split(',')[0])
    point1_y = int(point1.split(',')[1])
    point2_x = int(point2.split(',')[0])
    point2_y = int(point2.split(',')[1])

    coords = []

    starting_x_point = min(point1_x, point2_x)
    starting_y_point = min(point1_y, point2_y)
    ending_x_point = max(point1_x, point2_x)
    ending_y_point = max(point1_y, point2_y)

    if point1_x == point2_x:
        for i in range(starting_y_point, ending_y_point + 1):
            coords.append((point1_x, i))
    elif point1_y == point2_y:
        for i in range(starting_x_point, ending_x_point + 1):
            coords.append((i, point2_y))
    elif ending_x_point - starting_x_point == ending_y_point - starting_y_point:
        slope = (point1_x - point2_x) / (point1_y - point2_y)
        if slope == 1:
            for i in range(0, ending_x_point-starting_x_point + 1):
                coords.append((starting_x_point + i, starting_y_point + i))
        elif slope == -1:
            for i in range(0, ending_x_point-starting_x_point + 1):
                coords.append((starting_x_point + i, ending_y_point - i))

    return coords


def process_coords(coord):
    point1 = coord.split('->')[0].strip()
    point2 = coord.split('->')[1].strip()
    point1_x = int(point1.split(',')[0])
    point1_y = int(point1.split(',')[1])
    point2_x = int(point2.split(',')[0])
    point2_y = int(point2.split(',')[1])

    coords = []

    if point1_x == point2_x:
        for i in range(min(point1_y, point2_y), max(point1_y, point2_y) + 1):
            coords.append((point1_x, i))
    elif point1_y == point2_y:
        for i in range(min(point1_x, point2_x), max(point1_x, point2_x) + 1):
            coords.append((i, point2_y))

    return coords


def update_sea_floor_map(coords, sea_floor_map, overlap_points):
    for coord in coords:
        row = sea_floor_map[coord[1]]
        value = row.get(coord[0], 0)
        new_value = value + 1
        row[coord[0]] = new_value
        if new_value == 2:
            overlap_points += 1
    return overlap_points


def print_sea_floor_map(sea_floor_map):
    for x in range(0, 10):
        row = ''
        for y in range(0,10):
            row += str(sea_floor_map[x].get(y, '.'))
        print(row)


def part_one(input_data):
    sea_floor_map = defaultdict(dict)
    overlap_points = 0
    for coord in input_data:
        coords = process_coords(coord)
        overlap_points = update_sea_floor_map(coords, sea_floor_map, overlap_points)
    return overlap_points


def part_two(input_data):
    sea_floor_map = defaultdict(dict)
    overlap_points = 0
    for coord in input_data:
        coords = process_coords_diags(coord)
        overlap_points = update_sea_floor_map(coords, sea_floor_map, overlap_points)
    return overlap_points


if __name__ == "__main__":
    input_data = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]
    input_data = [x.decode() for x in get_input_for_day(5)]
    part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
