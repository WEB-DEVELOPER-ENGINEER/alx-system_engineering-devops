#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1]))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(sys.argv[1]))
    todos = todos.json()
    todoUser = {}
    taskList = []
    for task in todos:
        taskDict = {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')}
        taskList.append(taskDict)
    todoUser[sys.argv[1]] = taskList
    filename = sys.argv[1] + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
