'''
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added task: {new_task}")

def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to delete: "))
            delete_task(tasks, task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
'''



try:
    with open("todo.txt","r+") as tdfile:
except FileNotFoundError:
    return []

def add_data(self):
    append=input("Enter the data,you need to add: "))



def del_data():

def read_data():

'''
