from task_manager import *

while True:
    menu()
    op = input("Choose an option: ")

    if op == "1":
        task = input("Enter the task: ")
        print(save_task(task))
        clear()

    elif op == "2":
        list_tasks()
        clear()

    elif op == "3":
        id = input("Task ID: ")
        complete_task(id)
        clear()

    elif op == "4":
        id = input("Task ID: ")
        delete_task(id)
        clear()

    elif op == "0":
        print("Exiting...")
        break

    else:
        print("Invalid option")
        clear()