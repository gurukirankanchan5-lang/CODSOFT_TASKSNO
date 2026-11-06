

import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, 1):
        mark = "x" if t["done"] else " "
        print(f"  {i}. [{mark}] {t['title']}")


def get_index(tasks, prompt):
    if not tasks:
        print("\nNo tasks yet.")
        return None
    show_tasks(tasks)
    try:
        n = int(input(prompt))
    except ValueError:
        print("Please enter a number.")
        return None
    if 1 <= n <= len(tasks):
        return n - 1
    print("Invalid task number.")
    return None


def add_task(tasks):
    title = input("Task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def update_task(tasks):
    i = get_index(tasks, "Task number to update: ")
    if i is None:
        return
    title = input("New title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks[i]["title"] = title
    save_tasks(tasks)
    print("Task updated.")


def complete_task(tasks):
    i = get_index(tasks, "Task number to mark done: ")
    if i is None:
        return
    tasks[i]["done"] = True
    save_tasks(tasks)
    print("Marked as done.")


def delete_task(tasks):
    i = get_index(tasks, "Task number to delete: ")
    if i is None:
        return
    removed = tasks.pop(i)
    save_tasks(tasks)
    print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()
    actions = {
        "1": lambda: show_tasks(tasks),
        "2": lambda: add_task(tasks),
        "3": lambda: update_task(tasks),
        "4": lambda: complete_task(tasks),
        "5": lambda: delete_task(tasks),
    }
    while True:
        print("\n=== To-Do List ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task done")
        print("5. Delete task")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()