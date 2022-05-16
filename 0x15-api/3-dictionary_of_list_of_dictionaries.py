#!/usr/bin/python3
""" This is a module that gathers data from an API """

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    # Gets all users
    users = requests.get("{}users".format(url)).json()
    # jasonizes the users
    file = {}
    for user in users:
        # iterates over users and gets all their
        # "key values"
        userId = user.get("id")
        username = user.get("username")
        todos = requests.get("{}users/{}/todos".format(url, userId)).json()
        all_tasks = [{"username": username,
                      "task": all_tasks.get("title"),
                      "completed": all_tasks.get("completed"),
                      } for all_tasks in todos]
        file[userId] = all_tasks
        # to each user, add a key value pair
    with open("todo_all_employees.json", 'w') as filejs:
        json.dump(file, filejs)
        # prints to file
