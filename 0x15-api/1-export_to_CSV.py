#!/usr/bin/python3
""" Make an api request """
import requests
from sys import argv
import csv

# The API endpoint
base_url = "https://jsonplaceholder.typicode.com"


def fetch_employee_data(_id):
    user = requests.get(f"{base_url}/users/{_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={_id}").json()
    csv_filename = 'USER_ID.csv'

    done = []
    total = 0
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user['id'], user['name'], todo['completed'], todo['title']])
            total += 1
            if todo['completed']:
                done.append(todo['title'])

    print(f"Employee {user['name']} is done with tasks({len(done)}/{total}):")
    for task in done:
        print(f"\t {task}")


if __name__ == "__main__":
    fetch_employee_data(argv[1])
