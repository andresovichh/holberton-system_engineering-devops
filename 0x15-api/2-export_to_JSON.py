#!/usr/bin/python3
""" This is a module that gathers data from an API """

import json
import requests
from sys import argv


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    r = requests.get(url).json()
    t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(argv[1]))
    t = t.json()
    with open("{}.json".format(argv[1]), "w") as f:
        tasks = []

        for task in t:
            tasks.append({"task": task.get('title'),
                         "completed": task.get('completed'),
                          "username": r.get('username')})
        final = {"{}".format(argv[1]): tasks}
        json.dump(final, f)
