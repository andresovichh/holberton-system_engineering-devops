#!/usr/bin/python3
""" This is a module that gathers data from an API """

import requests
from sys import argv
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get("{}/{}".format(url, argv[1]))
    name = r.json().get('name')

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(argv[1]))
    todos = json.loads(req.text)
    tasks = len(todos)
    print(todos)
    # print(tasks)
    count = 0
    incompl = 0
    task_ist = []
    for task in todos:
        if task.get('completed') is True:
            count += 1
            task_ist.append(task)
        else:
            incompl += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, count, tasks))

    for task in task_ist:
        print("\t", task.get('title'))
