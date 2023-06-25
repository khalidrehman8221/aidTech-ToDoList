import json


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            return True
        else:
            return False

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Current tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.tasks, file)
        print(f"Tasks saved to {filename}.")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error occurred while loading tasks: {str(e)}")


def display_menu():
    print("\nTo-Do List Menu")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. View tasks")
    print("4. Save tasks")
    print("5. Load tasks")
    print("6. Quit")


todo_list = ToDoList()

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.add_task(task)
        print("Task added.")

    elif choice == '2':
        todo_list.view_tasks()
        task_index = int(input("Enter the task number to delete: "))
        if todo_list.delete_task(task_index):
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == '3':
        todo_list.view_tasks()

    elif choice == '4':
        filename = input("Enter the filename to save tasks: ")
        todo_list.save_tasks(filename)

    elif choice == '5':
        filename = input("Enter the filename to load tasks: ")
        todo_list.load_tasks(filename)

    elif choice == '6':
        print("Exiting the To-Do List...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

