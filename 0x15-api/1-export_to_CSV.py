#!/usr/bin/python3
"""
This is a module that gathers data from an API
and exports it to a CSV file """

import csv
import json
import pandas as pd
import requests
from sys import argv

if __name__ == '__main__':
    """ adding some documentation 
    to this dfile"""

    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get("{}/{}".format(url, argv[1]))
    name = r.json().get('name')

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(argv[1]))
    todos = json.loads(req.text)
    tasks = len(todos)
    # print(tasks)
    if name is not None:
        with open("{}.csv".format(argv[1]), "w", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([argv[1], r.json().get('username'),
                                task.get('completed'),
                                task.get('title')])
