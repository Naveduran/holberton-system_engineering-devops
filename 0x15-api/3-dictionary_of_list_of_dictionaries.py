#!/usr/bin/python3
"""Creates an json file with the tasks information for a given
employee ID, using an REST API
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    big_dict = {}
    for user in users:
        tasks_list = []
        employee_id = user.get('id')
        todos_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                employee_id)).json()
        for item in todos_list:
            dictt = {}
            dictt.update({"username": user.get('username')})
            dictt.update({"task": item.get('title')})
            dictt.update({"completed": item.get('completed')})
            tasks_list.append(dictt)
        big_dict.update({employee_id: tasks_list})

    with open("todo_all_employees.json", 'w') as f:
        f.write(json.dumps(big_dict))
