#!/usr/bin/python3
"""Creates an json file with the tasks information for a given
employee ID, using an REST API
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    employee_id = argv[1]

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(
            employee_id)).json()[0]
    todos_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id)).json()

    tasks_list = []
    for item in todos_list:
        dictt = {}
        dictt.update({"task": item.get('title')})
        dictt.update({"completed": item.get('completed')})
        dictt.update({"username": user.get('username')})
        tasks_list.append(dictt)
    big_dict = {employee_id: tasks_list}
    filename = "{}.json".format(employee_id)

    with open(filename, 'w') as f:
        f.write(json.dumps(big_dict))
