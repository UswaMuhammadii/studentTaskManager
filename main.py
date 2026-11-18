
print("Welcome to Student Task Manager!")

tasks = []

while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        if task.strip() == "":
            print("Error: Task title cannot be empty!")
        else:
            tasks.append(task)
            print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
