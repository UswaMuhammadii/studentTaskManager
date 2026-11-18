
print("Welcome to Student Task Manager!")

tasks = []

while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ").strip()

        if task == "":
            print("Error: Task title cannot be empty!")
        else:
            tasks.append({"title": task, "completed": False})
            print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                status = "Completed" if tasks[i]["completed"] else "Pending"
                print(f"{i + 1}. {tasks[i]['title']} - {status}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
