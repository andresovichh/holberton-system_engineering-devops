#!/usr/bin/python3
""" This is a module that gathers data from an API """

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    rq = requests.get("{}{}".format(url, argv[1]))

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(argv[1]))
    todos = req.json()
    user = rq.json()

    with open("{}.json".format(argv[1]), "w") as f:
        tasks = []

        for task in todos:
            tasks.append({"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": user.get('username')})
        final = {"{}".format(argv[1]): tasks}
        json.dump(final, f)
