import sys
import os
import json

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "status": "pending"})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks(filter_by=None):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if filter_by is None or task["status"] == filter_by:
            print(f"{i}. {task['description']} [{task['status']}]")

def update_task(index, new_description):
    tasks = load_tasks()
    try:
        tasks[index]["description"] = new_description
        save_tasks(tasks)
        print(f"Task {index} updated to: {new_description}")
    except IndexError:
        print("Error: Task index out of range.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    except IndexError:
        print("Error: Task index out of range.")

def mark_task(index, status):
    tasks = load_tasks()
    try:
        if status not in ["pending", "in progress", "done"]:
            print("Error: Invalid status. Use 'pending', 'in progress', or 'done'.")
            return
        tasks[index]["status"] = status
        save_tasks(tasks)
        print(f"Task {index} marked as {status}.")
    except IndexError:
        print("Error: Task index out of range.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py add <task_description>")
        else:
            add_task(sys.argv[2])

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif sys.argv[2] in ["done", "pending", "in progress"]:
            list_tasks(sys.argv[2])
        else:
            print("Invalid list filter. Use: done, pending, or in progress.")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py update <index> <new_description>")
        else:
            update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_tracker.py delete <index>")
        else:
            delete_task(int(sys.argv[2]))

    elif command == "mark":
        if len(sys.argv) < 4:
            print("Usage: python task_tracker.py mark <index> <status>")
        else:
            mark_task(int(sys.argv[2]), sys.argv[3])

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
