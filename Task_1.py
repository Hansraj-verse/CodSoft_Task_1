# ==========================================
# Task 1: To-Do List Application
#
# Objective:
# Create a Python application that allows users
# to manage and organize their daily tasks.
#
# Features:
# - Add Tasks
# - View Tasks
# - Update Tasks
# - Delete Tasks
# - Mark Tasks as Completed
# - Track Task Status
# - Menu Driven Interface
#
# ==========================================

# List to store tasks
tasks = []


# Function to add a new task
def add_task():
    task_name = input("\nEnter task name: ").strip()

    if task_name == "":
        print("Task name cannot be empty.")
        return

    task = {
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)
    print("Task added successfully.")


# Function to display all tasks
def view_tasks():
    print("\n========== TO-DO LIST ==========")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} [{task['status']}]")

    print("================================")


# Function to update an existing task
def update_task():
    if not tasks:
        print("\nNo tasks available to update.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to update: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        new_name = input("Enter new task name: ").strip()

        if new_name == "":
            print("Task name cannot be empty.")
            return

        tasks[task_number - 1]["name"] = new_name

        print("Task updated successfully.")

    except ValueError:
        print("Please enter a valid number.")


# Function to delete a task
def delete_task():
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(task_number - 1)

        print(f"Task '{removed_task['name']}' deleted successfully.")

    except ValueError:
        print("Please enter a valid number.")


# Function to mark task as completed
def mark_completed():
    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_number - 1]["status"] = "Completed"

        print("Task marked as completed.")

    except ValueError:
        print("Please enter a valid number.")


# Function to display menu
def show_menu():
    print("\n========== TO-DO LIST MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("=====================================")


# Main program loop
def main():
    print("Welcome to the To-Do List Application")

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            mark_completed()

        elif choice == "6":
            print("\nThank you for using the To-Do List Application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


# Program execution starts here
if __name__ == "__main__":
    main()