import json
import os


def menu():
    print("\n==== TASK MANAGER ====")
    print("1 - Add task")
    print("2 - View tasks")
    print("3 - Complete task")
    print("4 - Delete task")
    print("0 - Exit")


def clear():
    input("Press Enter to continue...")
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def load_json():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return {}


def save_task(task):
    tasks = load_json()

    id = str(len(tasks) + 1)

    tasks[id] = {
        "task": task,
        "status": "In progress"
    }

    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    return "Task added successfully"


def list_tasks():
    tasks = load_json()

    if not tasks:
        print("No tasks found.")
        return

    print("\n===== TASK LIST =====")

    for a in tasks:
        task = tasks[a]["task"]
        status = tasks[a]["status"]

        print(f"[{a}] {task} | Status: {status}")


def delete_task(id):
    tasks = load_json()

    id = str(id)

    if id in tasks:
        del tasks[id]

        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)

        print("Task removed")
    else:
        print("Task not found")


def complete_task(id):
    tasks = load_json()

    id = str(id)

    if id in tasks:
        tasks[id]["status"] = "Completed"

        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=4)

        print("Task completed.")
    else:
        print("Task not found")