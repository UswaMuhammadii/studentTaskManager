
print("Welcome to Student Task Manager!")

tasks = []

while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

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
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['title']}")

            try:
                task_id = int(input("Enter task number to complete: "))

                if 1 <= task_id <= len(tasks):
                    if tasks[task_id - 1]["completed"]:
                        print("Task is already completed!")
                    else:
                        tasks[task_id - 1]["completed"] = True
                        print("Task marked as completed!")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['title']}")

            try:
                task_id = int(input("Enter task number to delete: "))

                if 1 <= task_id <= len(tasks):
                    deleted_task = tasks.pop(task_id - 1)
                    print(f"Task '{deleted_task['title']}' deleted successfully!")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
