import os
import json
import sys
from datetime import datetime, timedelta
import platform
script_dir = os.path.dirname(os.path.abspath(__file__))
tasks_file = os.path.join(script_dir, "tasks.json")

def adjust_priority(task):
    now = datetime.now()
    due_date = datetime.strptime(task["due_date"], "%d-%m-%Y %H:%M")
    priority_map = {"Low":1, "Med":2, "High":3,}
    reverse_map = {1: "Low", 2:"Med", 3:"High",}
    current_priority = priority_map.get(task["priority"], 1)
    if now >= due_date - timedelta(days=1):
        current_priority = min(current_priority + 1, 3,)
    if now >= due_date - timedelta(hours=1):
        current_priority = min(current_priority + 1, 3,)
    task["priority"] = reverse_map[current_priority]
    return task

def get_due_date():
    while True:
        date_input = input("Enter the due date & time (DD-MM-YYYY HH:MM):\n")
        if date_input.lower() == "menu":
            clear_screen()
            beep_error()
            print("Aborting entry, taking you back to main menu...")
            main_menu()
        try:
            due_date = datetime.strptime(date_input, "%d-%m-%Y %H:%M")
            now = datetime.now()
            if due_date <= now:
                beep_error()
                clear_screen()
                print("Must be a future date & time, try again...\n")
                print("You can type 'menu' to abort\n")
                continue
            return due_date
        except ValueError:
            beep_error()
            clear_screen()
            print("Invalid format! Please enter date like DD-MM-YYYY HH:MM")

def get_next_id(tasks):
    if not tasks:
        return 1
    else:
        max_id = max(task["id"] for task in tasks)
        return max_id + 1

def load_data():
    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w') as f:
            json.dump({"tasks":[]},f, indent=4)
    with open(tasks_file,'r') as f:
        return json.load(f)

def save_data(data):
    with open(tasks_file, 'w') as f:
        json.dump(data, f, indent=4)

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
def beep_error():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000,150)
    else:
        print("\a")

def beep_success():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(400,500)
    else:
        print("\a\a\a")

def add_task():
    clear_screen()
    while True:
        print("*ADDING A TASK*\n")
        task_name = input("What's the title of the task?:\n").capitalize()
        while True:
            task_priority = input("How important is this task? (Low, Med, High)?:\n").capitalize()
            if task_priority in ["Low","Med","High"]:
                break
            elif task_priority == 'Menu':
                clear_screen()
                print("Aborting function, taking you back to main menu...")
                main_menu()
            else:
                clear_screen()
                beep_error()
                print("Invalid entry, enter 'Low','Med', or 'High':\n")
                print("You can also type 'menu' to go back to main menu and abort...\n")
        task_description = input("Describe the task in more detail or include some notes:\n").capitalize()
        task_date = get_due_date()
        task_date_str = task_date.strftime("%d-%m-%Y %H:%M")
        clear_screen()
        print(f"Task Title: {task_name}")
        print(f"Task Priority: {task_priority}")
        print(f"Description: {task_description}")
        print(f"Due Date: {task_date_str}")
        print("  ")
        while True:
            option = input("Would you like to add this task?\n").upper()
            clear_screen()
            if option == "YES":
                data = load_data()
                task_list = data["tasks"]
                new_task = {
                    "id": get_next_id(task_list), 
                    "title": task_name,
                    "priority": task_priority,
                    "description": task_description,
                    "due_date": task_date_str,
                    "completed": False
                }
                data["tasks"].append(new_task)
                save_data(data)
                beep_success()
                print("This task has now been added, taking you back to menu...")
                main_menu()
            elif option == "NO":
                print("This task has NOT been added.\n")
                while True:
                    option1 = input("Would you like to try adding the task again?\n").upper()
                    if option1 == "YES":
                        clear_screen()
                        print("Great, let's try adding the task again...")
                        add_task()
                    elif option1 == "NO":
                        clear_screen()
                        print("Let's take you back to the main menu")
                        main_menu()
                    else:
                        beep_error()
                        clear_screen()
                        print("Please enter either 'Yes' or 'No'\n")
            else:
                beep_error()
                print("Please enter either 'Yes' or 'No'\n")

def view_all_tasks():
    data = load_data()
    tasks = data["tasks"]
    tasks = [adjust_priority(task) for task in tasks]
    priority_map = {"Low": 1, "Med": 2, "High": 3}
    tasks.sort(key=lambda t: (-priority_map[t["priority"]], datetime.strptime(t["due_date"], "%d-%m-%Y %H:%M")))
    if not tasks:
        clear_screen()
        beep_error()
        print("You don't have any tasks at all, try adding a new task.\n")
        main_menu()
    else:
        for task in tasks:
            print("-" * 50)
            print(f'ID: {task["id"]} | Title: {task["title"]} | Priority: {task["priority"]} | Due: {task["due_date"]} | Completed: {task["completed"]}')
            print("Task Description:\n")
            print(f"{task['description']}")
            print("-" * 50)
    input("Press enter to return to main menu")
    clear_screen()

def find_task(tasks, search):
    if search.isdigit():
        task_id = int(search)
        for task in tasks:
            if task["id"] == task_id:
                return task
    else:
        for task in tasks:
            if task["title"].lower() == search.lower():
                return task
    return None

def delete_task():
    print("*DELETING A TASK*\n")
    data = load_data()
    tasks = data["tasks"]

    if not tasks:
        beep_error()
        print("No tasks found, please add tasks first.\n")
        main_menu()

    while True:
        search = input("Enter the Task ID or the task title to delete:\n").capitalize()
        if search.lower() == "menu":
             beep_error()
             clear_screen()
             print("Taking you back to main menu...")
             main_menu()
        task = find_task(tasks, search)
        if task is None:
            beep_error()
            clear_screen()
            print("No tasks found with those details, try again.\n")
        else:
            clear_screen()
            beep_success()
            print("Task found!:")
            print(f"Task ID: {task['id']}")
            print(f"Task Title: {task['title']}")
            print(f"Task Description: {task['description']}")
            print(f"Task Due Date: {task['due_date']}")
            print(f"Task Complete Status: {task['completed']}\n")
            while True:
                if task["completed"] == True:
                    print("Do you wish to continue to delete this task?")
                    confirm = input("Type 'Yes' or 'No'\n").upper()
                    if confirm == "YES":
                        beep_success()
                        tasks.remove(task)
                        save_data(data)
                        clear_screen()
                        print(f"The task '{task['title']}' has been deleted!\n")
                        print("Taking you back to the main menu\n")
                        main_menu()
                    elif confirm == "NO":
                        beep_error()
                        clear_screen()
                        print(f"The task '{task['title']}' has NOT been deleted\n")
                        print("Taking you back to main menu...\n")
                        main_menu()
                    else:
                        beep_error()
                        clear_screen()
                        print("You are deleting the following task:\n")
                        print(f"Task ID: {task['id']}")
                        print(f"Task Title: {task['title']}\n")
                        print("Please type either 'Yes' or 'No':\n")
                else:
                    print("This task is still incomplete")
                    confirm = input("Are you sure you would like to delete?\n").upper()
                    if confirm == "YES":
                        beep_success()
                        tasks.remove(task)
                        save_data(data)
                        clear_screen()
                        print(f"The task '{task['title']}' has been deleted!\n")
                        print("Taking you back to the main menu\n")
                        main_menu()
                    elif confirm == "NO":
                        beep_error()
                        clear_screen()
                        print(f"The task '{task['title']}' has NOT been deleted\n")
                        print("Taking you back to main menu...\n")
                        main_menu()
                    else:
                        beep_error()
                        print("Please enter either 'Yes' or 'No'")

def task_complete():
    clear_screen()
    print("*MARKING TASK AS COMPLETE*\n")
    data = load_data()
    tasks = data["tasks"]
    if not tasks:
        clear_screen()
        print("No tasks available to mark as complete :(.\n")
        main_menu()
    search = input("Enter the task ID or title to mark as complete: \n")
    task = find_task(tasks, search)
    if task is None:
        beep_error()
        clear_screen()
        print("No tasks found with those details, try again.")
        main_menu()
    if task in tasks and task['completed'] == True:
        clear_screen()
        beep_error()
        print(f"Task '{task['title']}' is already completed :).")
        main_menu()
    if task in tasks and task["completed"] == False:
        task["completed"] = True
        save_data(data)
        beep_success()
        clear_screen()
        print(f"Task '{task['title']}' has been updated to complete! :)")
        main_menu()
def modify_task():
    clear_screen()
    print("*MODIFYING A TASK*")
    print("Hint: you can type 'menu' to abort")
    data = load_data()
    tasks = data["tasks"]
    if not tasks:
        beep_error()
        clear_screen()
        print("You don't have any tasks right now, try adding a task first.")
        main_menu()
    while True:
        search = input("Enter task name or ID: \n").capitalize()
        if search == "Menu":
            clear_screen()
            print("Taking you back to the main menu...\n")
            main_menu()
        task = find_task(tasks, search)
        if task is None:
            beep_error()
            clear_screen()
            print("There is no task with those details, try again or enter 'menu' to go back.")
        elif task in tasks:
            clear_screen()
            print(f"*MODIFYING TASK DETAILS*")
            print("Found it!\n")
            print(f"Task ID: {task['id']}")
            print(f"Task Title: {task['title']}\n")
            print("1. Change Task Title.")
            print("2. Change Task Due Date.")
            print("3. Change Task Description.")
            print("4. Change Task Priority.")
            print("5. Change task to edit.")
            print("6. Main Menu\n")
            option = input("Select from the option above:\n")
            while True:
                if option == '1':
                    clear_screen()
                    print("*CHANGING TASK TITLE*\n")
                    print(f"Changing the title of '{task['title']}'\n")
                    new_title = input(f"What would you like the new title to be?\n").capitalize()
                    print(" ")
                    confirm = input(f"Just to confirm, you would like to change: '{task['title']}' to '{new_title}'?\n").upper()
                    if confirm == 'YES':
                        task["title"] = new_title
                        save_data(data)
                        beep_success()
                        clear_screen()
                        print("Task updated successfully.")
                        main_menu()
                    if confirm == 'NO':
                        clear_screen()
                        print("You have chose to abort change, back to main menu.")
                        main_menu()
                elif option == '2':
                    clear_screen()
                    print("*CHANGING DUE DATE*\n")
                    print("Tasks' Current Details:\n")
                    print(f"Task ID: {task['id']}")
                    print(f"Task Title: {task['title']}")
                    print(f"Task Due Date: {task['due_date']}")
                    print("  ")
                    print("Provide the new date below:")
                    task_date = get_due_date()
                    new_date = task_date.strftime("%d-%m-%Y %H:%M")
                    clear_screen()
                    print("Just to confirm, you would like to change the dates")
                    print(f"FROM: '{task['due_date']}' TO: '{new_date}'\n")
                    print(f"Of task: {task['title']} with ID: {task['id']}?\n")
                    confirm = input("Enter 'Yes' or 'No'\n").upper()
                    if confirm == 'YES':
                        clear_screen()
                        task["due_date"] = new_date
                        save_data(data)
                        beep_success()
                        print("Task updated successfully.")
                        main_menu()
                    elif confirm == 'NO':
                        clear_screen()
                        print("You have chose to abort, let's take you back to main menu")
                        main_menu()
                    else:
                        print("Invalid entry, type 'Yes' or 'No'")
                elif option == '3':
                    clear_screen()
                    print("*CHANGING DESCRIPTION*\n")
                    print("Tasks details:")
                    print(f"Task ID: {task['id']}")
                    print(f"Task Title: {task['title']}")
                    print(f"Current Task Description:\n")
                    print(f"{task['description']}")
                    print("-" * 50)
                    new_description = input(f"Type new task description:\n").capitalize()
                    clear_screen()
                    print("The old task description:\n")
                    print(f"'{task['description']}'")
                    print("-" * 50)
                    print("The new task description:\n")
                    print(f"'{new_description}'\n")
                    while True:
                        confirm = input(f"Confirm change ('Yes' or 'No')?\n").upper()
                        if confirm == 'YES':
                            clear_screen()
                            task["description"] = new_description
                            save_data(data)
                            beep_success()
                            print("Task updated successfully.")
                            main_menu()
                        elif confirm == 'NO':
                            clear_screen()
                            beep_error()
                            print("You have chose to cancel this, let's take you back to main menu")
                            main_menu()
                        else:
                            beep_error()
                            clear_screen()
                            print("New task description to be:\n")
                            print(f"'{new_description}'\n")
                            print(f"For task:")
                            print(f"ID: {task['id']}")
                            print(f"TITLE: {task['title']}\n")
                            print("Invalid entry, please type either 'Yes' or 'No'")
                elif option == '4':
                    clear_screen()
                    print("*CHANGING PRIORITY LEVEL*\n")
                    print("Task selected:\n")
                    print(f"Task ID: {task['id']}")
                    print(f"Task Title: {task['title']}\n")
                    print(f"Current Priority Level: {task['priority']}\n")
                    while True:
                        print("What's the new priority level?")
                        new_priority = input(f"(Low, Med, or High)\n").capitalize()
                        if new_priority in ["Low", "Med", "High"]:
                            clear_screen()
                            print("You would like to update the priority of the following task:")
                            print(f"Task ID: {task['id']}")
                            print(f"Task Title: {task['title']}\n")
                            print(f"FROM: {task['priority']}")
                            print(f"TO: {new_priority}?\n")
                            while True:
                                confirm = input(f"Please type either 'Yes' or 'No'\n").upper()
                                if confirm == 'YES':
                                    task["priority"] = new_priority
                                    save_data(data)
                                    beep_success()
                                    clear_screen()
                                    print("Task updated successfully.")
                                    main_menu()
                                if confirm == 'NO':
                                    beep_error()
                                    clear_screen()
                                    print("You have chose to abort change, back to main menu...")
                                    main_menu()
                                else:
                                    beep_error()
                                    clear_screen()
                                    print("Invalid entry!\n")
                        else:
                            beep_error()
                            clear_screen()
                            print("Invalid entry, please try again")
                elif option == '5':
                    clear_screen()
                    modify_task()
                elif option == '6':
                    clear_screen()
                    main_menu()
                else:
                    beep_error()
                    print("Invalid entry!")
                    modify_task()
        else:
            print("Invalid entry!")
            main_menu()
def main_menu():
    while True:
        print("  ")
        print("1. Add New Task")
        print("2. Modify a Task")
        print("3. Mark Task as Complete")
        print("4. Delete a Task")
        print("5. View All Tasks")
        print("6. Close Application.")
        print("  ")
        option = input("What would you like to do? :\n").lower()
        if option == '1':
            add_task()
        elif option == '2':
            modify_task()
        elif option == '3':
            task_complete()
        elif option == '4':
            clear_screen()
            delete_task()
        elif option == '5':
            view_all_tasks()
        elif option in ["exit", '6']:
            exit()
        else:
            clear_screen()
            beep_error()
            print("!!! Please only enter from the list below: !!!")

main_menu()
