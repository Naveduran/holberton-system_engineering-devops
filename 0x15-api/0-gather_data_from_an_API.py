#!/usr/bin/python3
"""Returns information about his/her TODO list progress.
Using a REST API, for a given employee ID
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_id = argv[1]

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(
            employee_id)).json()[0]
    todos_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)).json()

    completed = []
    for item in todos_list:
        if item.get('completed'):
            completed.append(item)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos_list)))

    for item in completed:
        print("\t {}".format(item.get("title")))
