import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
        return
    print("\n Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = " Done" if task["done"] else " Not Done"
        print(f"{i}. {task['task']} [{status}]")

def add_task(tasks):
    task_text = input("Enter new task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        print(" Task added.")
    else:
        print(" Empty task not added.")

def mark_done(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(" Task marked as done.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n Daily Task Tracker Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Save & Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("📁 Tasks saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")


main()
