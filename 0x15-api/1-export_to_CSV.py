#!/usr/bin/python3
"""Creates an csv file with the tasks information for a given
employee ID, using an REST API
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

    text = ""
    for item in todos_list:
        t = '"{}","{}","{}","{}"\n'.format(
            employee_id,
            user.get('username'),
            item.get('completed'),
            item.get('title')
        )
        text += t

    filename = "{}.csv".format(employee_id)

    with open(filename, 'w') as f:
        f.write(text)
