#!/usr/bin/python3
""" Make a json file conataining api request """
import json
import requests

# The API endpoint
base_url = "https://jsonplaceholder.typicode.com"


def fetch_employee_data():
    user = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()
    json_filename = "todo_all_employees.json"

    todos_details = []
    for todo in todos:
        deets = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user['username']
                }
        todos_details.append(deets)

    data = {user['id']: todos_details}
    json_string = json.dumps(data)
    print(json_string)
#    with open(json_filename, 'w') as json_file:
#        json_file.write(json_string)


if __name__ == "__main__":
    fetch_employee_data()
