#!/usr/bin/python3
""" This is a module that gathers data from an API """

import requests
from sys import argv
import json
import csv
import pandas as pd

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get("{}/{}".format(url, argv[1]))
    name = r.json().get('name')

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(argv[1]))
    todos = json.loads(req.text)
    tasks = len(todos)
    # print(tasks)
    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([argv[1], r.json().get('username'),
                             task.get('completed'),
                             task.get('title')])
