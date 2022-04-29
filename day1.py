#! /usr/bin/python

from get_input import get_input_for_day

def part_one(input_data):
    previous_distance = 10000000
    larger_distance_count = 0
    for distance in input_data:
        if distance > previous_distance:
            larger_distance_count += 1
        previous_distance = distance
    print(larger_distance_count)

def part_two(input_data):
    larger_sum_count = 0
    previous_sum = input_data[0] + input_data[1] + input_data[2]
    for i in range(3, len(input_data)):
        distance_sum = input_data[i] + input_data[i-1] + input_data[i-2]
        if distance_sum > previous_sum:
            larger_sum_count += 1
        previous_sum = distance_sum
    print(larger_sum_count)




if __name__ == "__main__":
    input_data = get_input_for_day(1)
    part_one(input_data)
    part_two(input_data)
