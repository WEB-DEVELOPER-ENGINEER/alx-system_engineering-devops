#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
            format(sys.argv[1]))
    name = response.json().get('name')
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
            format(sys.argv[1]))
    j = 0
    for i in response.json():
        if i.get('completed') is True:
            j += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, j, len(response.json())))
    for i in response.json():
        print('\t {}'.format(i.get('title')))
