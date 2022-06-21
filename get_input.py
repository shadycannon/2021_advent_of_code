#!/usr/bin/python3

import requests


def get_input_for_day(day):
    url = f'https://adventofcode.com/2021/day/{day}/input'
    headers = {
        "cookie": "_ga=GA1.2.420815534.1651203263; _gid=GA1.2.134528181.1655833616; _gat=1; session=53616c7465645f5f7b24da1b5bbf0133acc8e6a8c2213829397924f37af1b961b0925214e786cb8c950ba382c4d44a3991587482fd34f56a004b0b52dbd927ee"
    }
    response = requests.get(url=url, headers=headers, verify=False)
    response.raise_for_status
    input_data = []
    for line in response.iter_lines():
        input_data.append(line)
    return input_data


if __name__ == "__main__":
    print(get_input_for_day(1))
