#!/usr/bin/python3

import requests


def get_input_for_day(day):
    url = f'https://adventofcode.com/2021/day/{day}/input'
    headers = {
        "cookie": "SECRET"
    }
    response = requests.get(url=url, headers=headers, verify=False)
    response.raise_for_status
    input_data = []
    for line in response.iter_lines():
        input_data.append(line)
    return input_data


if __name__ == "__main__":
    print(get_input_for_day(1))
