#!/usr/bin/python3
"""export data in the CSV format"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(sys.argv[1]))
    filename = sys.argv[1] + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            writer.writerow([sys.argv[1], name, str(task.get('completed')),
                                 task.get('title')])
