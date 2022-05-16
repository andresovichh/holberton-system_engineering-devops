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
    username = r.json().get('username')

    if username is not None:
        todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                           .format(argv[1])).json()
    # todos = json.loads(req.text)
    # print(tasks)
    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([argv[1],
                            username,
                            task.get('completed'),
                            task.get('title')])
    print(len(todos))