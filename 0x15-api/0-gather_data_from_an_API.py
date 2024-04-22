#!/usr/bin/python3
"""
Script to retrieve and display employee TODO list progress from the API.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays employee TODO list progress.
    """
    # Base URL of the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Endpoint for user details
    user_endpoint = f'{base_url}users/{employee_id}'

    # Endpoint for user's TODO list
    todo_endpoint = f'{base_url}todos?userId={employee_id}'

    # Retrieve user details
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Retrieve user's TODO list
    todo_response = requests.get(todo_endpoint)
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task.get('completed')]

    # Display progress
    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{len(todo_data)}):")
    
    # Display completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 employee_todo_progress.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

