#!/usr/bin/python3
""" This is a module that gathers data from an API """

import requests
from sys import argv
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get("{}/{}".format(url, argv[1]))
    name = r.json().get('name')
    r = json.loads(r.text)
    rj = json.dumps(r)

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(argv[1]))
    todos = json.loads(req.text)

    task = [task for task in todos]
    final = {argv[1]: []}

    for task in task:
        tasks_dict = {"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": name
                      }
        final[argv[1]].append(tasks_dict)
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(final, f)
