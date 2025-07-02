print("Welcome to todo list")

tasks = []

while True:
    print("\n1. Create a task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Remove a task")
    print("0. Exit")

    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")

    if option == 0:
        break
    elif option == 1:
        taskTitle = input("Enter task title: ")
        time = input("Enter time: ")
        tasks.append([taskTitle, time])
        print("Task successfully added")
    elif option == 2:
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task[0]} {task[1]}")
        else:
            print("No tasks available.")
    elif option == 3:
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task[0]} {task[1]}")
        else:
            print("No tasks available.")
        removeTask = int(input("Choose a task to complete : "))
        if 0 < removeTask <= len(tasks):
            tasks.pop(removeTask - 1)
        else:
            print("Invalid task number.")
        print("Task successfully complete")
    elif option == 4:
        if tasks:
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task[0]} {task[1]}")
        else:
            print("No tasks available.")
        removeTask = int(input("Choose a task to complete : "))
        tasks.pop(removeTask - 1)
    else:
        print("Invalid option.")