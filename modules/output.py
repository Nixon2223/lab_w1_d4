from modules.task_list import *

def print_task_descriptions(list):
    for task in list:
        print(task["description"])

def print_list(list):
    for task in list:
        print_task(task)

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken
    return task

def add_to_list(list, task):
    list.append(task)
 
def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("Q or q: Quit")