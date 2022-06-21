#! /usr/bin/python

from typing import List, Dict
from get_input import get_input_for_day
from collections import defaultdict, Counter
Path = Dict[str, List[str]]

class PathFinder:
    def __init__(self, input_data: List[str]) -> None:
        path_tuples = [(x.split('-')[0], x.split('-')[1]) for x in input_data]
        self.paths = defaultdict(list)
        self.valid_paths = []
        self.current_path = []

        for path in path_tuples:
            self.paths[path[0]].append(path[1])
            if path[1] != 'end' and path[0] != 'start':
                self.paths[path[1]].append(path[0])
        self.paths = dict(self.paths)

    def print_paths(self, subpath: Path = None) -> None:
        if subpath:
            paths = subpath
        else:
            paths = self.paths

        for path, values in paths.items():
            for value in values:
                print(f'{path} -> {value}')

    def get_sub_path(self, paths: Path, current_node: str) -> Path:
        subpath = {}
        for path, values in paths.items():
            if path == current_node:
                continue
            subpath[path] = values
        return subpath

    def is_small_cave_allowed(self, current_node: str) -> bool:
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

    def find_paths(self, current_node: str = 'start') -> bool:
        subpath = self.paths
        if current_node.islower() and current_node in self.current_path:
            return False
        if current_node == 'end':
            self.valid_paths.append(self.current_path + ['end'])
            return True
        values = subpath[current_node]

        self.current_path.append(current_node)

        for value in values:
            self.find_paths(value)
        self.current_path.pop()

    def find_paths_part_two(self, current_node: str = 'start') -> bool:
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

    def find_paths_no_globals(self, current_node: str = 'start', current_path: List[str] = []) -> bool:

        subpath = self.paths

        new_current_path = current_path[:]  # make a copy to essentially pass current_path in by value, not reference

        if current_node.islower() and current_node in new_current_path:
            return False

        if current_node == 'end':
            self.valid_paths.append(new_current_path + ['end'])
            return True

        values = subpath[current_node]

        new_current_path.append(current_node)

        for value in values:
            self.find_paths_no_globals(value, new_current_path)


    def part_one(self) -> None:
        print(self.paths)
        print(self.find_paths())
        print()
        print(len(self.valid_paths))

    def part_two(self) -> None:
        print(self.paths)
        print(self.find_paths_part_two())
        print(len(self.valid_paths))

    def no_globals(self) -> None:
        self.find_paths_no_globals()
        print(len(self.valid_paths))


if __name__ == "__main__":
    test_data = [
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
    pf.part_one()
    pf.part_two()
    pf.no_globals()
