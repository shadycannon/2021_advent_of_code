#! /usr/bin/python

from get_input import get_input_for_day
import math
from collections import Counter

DAYS = 256
REPRODUCTION_TIME = 7

def part_one(input_data):
    fishies = [int(x) for x in input_data[0].split(',')]
    for day in range(0, DAYS):
        for i in range(0, len(fishies)):
            fish = fishies[i]
            if fish == 0:
                fishies[i] = 6
                fishies.append(8)
            else:
                fishies[i] = fish - 1
        print(day)
    return len(fishies)

def part_two(input_data):
    total_fishies = 0
    fishies = Counter([int(x) for x in input_data[0].split(',')])
    print(fishies)
    for day in range(0, DAYS):
        new_fishies = {}
        for age, count in fishies.items():
            if age == 0:
                new_fishies[6] = count + new_fishies.get(6, 0)
                new_fishies[8] = count
            else:
                new_fishies[age - 1] = count + new_fishies.get(age-1, 0)
        fishies = new_fishies
        print(fishies)

    return(sum(fishies.values()))


if __name__ == "__main__":
    input_data = ["3,4,3,1,2"]
    #input_data = [x.decode() for x in get_input_for_day(6)]
    #part_one_answer = part_one(input_data)
    part_two_answer = part_two(input_data)
    #print(f'part_one_answer: {part_one_answer}')
    print(f'part_two_answer: {part_two_answer}')
