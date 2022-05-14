#! /usr/bin/python

from get_input import get_input_for_day
from itertools import permutations

from collections import defaultdict,Counter
from statistics import median


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextvals = []

class LinkedList:
    def __init__(self):
        self.headval = None

    def get_all_values(self):
        pass

class PathFinder:
    def __init__(self, input_data):
        path_tuples = [(x.split('-')[0], x.split('-')[1]) for x in input_data]
        self.paths = defaultdict(list)
        self.valid_paths = []
        self.current_path = []

        for path in path_tuples:
            self.paths[path[0]].append(path[1])
            if path[1] != 'end' and path[0] != 'start':
                self.paths[path[1]].append(path[0])
        self.paths = dict(self.paths)

    def print_paths(self, subpath = None):
        if subpath:
            paths = subpath
        else:
            paths = self.paths

        for path, values in paths.items():
            for value in values:
                print(f'{path} -> {value}')

    def get_sub_path(self, paths, current_node):
        subpath = {}
        for path, values in paths.items():
            if path == current_node:
                continue
            subpath[path] = values
        return subpath

    def is_small_cave_allowed(self, current_node):
        if not current_node.islower():
            return True
        if current_node not in self.current_path:
            return True

        c = Counter(self.current_path)
        for value, count in c.items():
            if value.islower():
                if count == 2:
                    return False


        return True


    def find_paths(self, current_node='start'):
        print('recursed')
        subpath = self.paths
        if current_node.islower() and current_node in self.current_path:
            print('lower twice')
            return False

        if current_node == 'end':
            print('end')
            self.valid_paths.append(self.current_path + ['end'])
            return True

        print(f'current path: {self.current_path}')

        values = subpath[current_node]
        print(f'vals:{values}')

        self.current_path.append(current_node)

        for value in values:
            print(f'val: {value}')
            self.find_paths(value)
        self.current_path.pop()


    def find_paths_part_two(self, current_node='start'):
        subpath = self.paths
        if current_node.islower() and current_node in self.current_path:
            if current_node == 'start':
                return False
            small_allowed = self.is_small_cave_allowed(current_node)
            if not small_allowed:
                return False


        if current_node == 'end':
            self.valid_paths.append(self.current_path + ['end'])
            return True

        values = subpath[current_node]

        self.current_path.append(current_node)

        for value in values:
            self.find_paths_part_two(value)
        self.current_path.pop()


    def find_paths_no_globals(self, current_node='start', current_path=[]):
        print('recursed')
        print(f'current node: {current_node}')
        print(f'current path b4: {current_path}')
        subpath = self.paths

        new_current_path = current_path[:]  # make a copy to essentially pass current_path in by value, not reference

        if current_node.islower() and current_node in new_current_path:
            print('lower twice')
            return False

        if current_node == 'end':
            print('end')
            self.valid_paths.append(new_current_path + ['end'])
            return True


        values = subpath[current_node]
        print(f'vals:{values}')

        new_current_path.append(current_node)
        print(f'current_path_after: {new_current_path}')

        for value in values:
            print(f'val: {value}')
            self.find_paths_no_globals(value, new_current_path)

        print('returned')


    def part_one(self):
        print(self.paths)
        print(self.find_paths())
        print()
        print(len(self.valid_paths))

    def part_two(self):
        print(self.paths)
        print(self.find_paths_part_two())
        print(len(self.valid_paths))
        #return self.get_sub_path(self.paths, 'start')

    def no_globals(self):
        self.find_paths_no_globals()
        print(len(self.valid_paths))


if __name__ == "__main__":
    input_data = [
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end',
    ]
    input_data = [x.decode() for x in get_input_for_day(12)]


    pf = PathFinder(input_data)
    pf.print_paths()
    #print(pf.part_one())
    #print(pf.part_two())
    print(pf.no_globals())
    #print(s.part_one())
    #print(s.num_flashes)
    #part_one_answer = part_one(input_data)
    #part_two_answer = part_two(input_data)
    #print(f'part_one_answer: {part_one_answer}')
    #print(f'part_two_answer: {part_two_answer}')
