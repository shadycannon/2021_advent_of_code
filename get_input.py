#!/usr/bin/python3

import requests


def get_input_for_day(day):
    url = f'https://adventofcode.com/2021/day/{day}/input'
    headers = {
        "cookie": "_ga=GA1.2.420815534.1651203263; _gid=GA1.2.1557776459.1651203263; session=53616c7465645f5ffbe748084ed354e3ac8a97a2e19c899441a48d4acb09313d4db755012bd63a6b11994420979c49570bef8cef8f1340e580718605276b9f3a"
    }
    response = requests.get(url=url, headers=headers, verify=False)
    response.raise_for_status
    input_data = []
    for line in response.iter_lines():
        input_data.append(line)
    return input_data


if __name__ == "__main__":
    print(get_input_for_day(1))
