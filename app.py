from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

def clear_list():
    user_input = input("Would you like to load task, YES or NO?: ").lower()
    if user_input == "no":
        tasks.clear()
    return tasks
    

clear_list()


while (True):
    print_menu()
    option = option_f()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = description_f()
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif option == '5':
        time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif option == '6':
        description =description_f()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = description_f_2()
        time_taken = time_taken_f()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")