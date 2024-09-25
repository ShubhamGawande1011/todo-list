to_do_list = []  # List to store tasks

while True:
    # Display menu
    print("\nTo-Do List")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':  # Add task
        task = input("Enter the task: ")
        to_do_list.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    elif choice == '2':  # View all tasks
        if not to_do_list:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, item in enumerate(to_do_list):
                status = "Completed" if item["completed"] else "Pending"
                print(f"{i+1}. {item['task']} [{status}]")

    elif choice == '3':  # Mark task as completed
        if not to_do_list:
            print("No tasks to mark as completed.")
        else:
            task_number = int(input("Enter the task number to complete: ")) - 1
            if 0 <= task_number < len(to_do_list):
                to_do_list[task_number]["completed"] = True
                print(f"Task '{to_do_list[task_number]['task']}' marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == '4':  # Delete task
        if not to_do_list:
            print("No tasks to delete.")
        else:
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_number < len(to_do_list):
                removed_task = to_do_list.pop(task_number)
                print(f"Task '{removed_task['task']}' deleted.")
            else:
                print("Invalid task number.")

    elif choice == '5':  # Exit
        print("Exiting the program.")
        break

    else:
        print("Invalid option, please choose between 1-5.")
