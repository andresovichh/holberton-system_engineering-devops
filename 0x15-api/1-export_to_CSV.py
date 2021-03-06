#!/usr/bin/python3
"""Exports results to a csv"""

import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get("{}/{}".format(url, argv[1]))
    username = r.json().get('username')

    if username is not None:
        t = requests.get("https://jsonplaceholder.typicode.com/users/{}/t"
                         .format(argv[1])).json()
    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in t:
            writer.writerow([argv[1],
                            username,
                            task.get('completed'),
                            task.get('title')])
