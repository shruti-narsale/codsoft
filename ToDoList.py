def todo_list():
    tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Update a task")
        print("4. Mark a task as complete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            print("Task added successfully!")
        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
            else:
                print("No tasks in the list yet.")
        elif choice == "3":
            if tasks:
                # Show complete to-do list and ask for task to update
                print("\nSelect the task to update:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")

                try:
                    task_index = int(input("Enter the number of the task to update: ")) - 1
                    updated_task = input("Enter the updated task: ")
                    tasks[task_index] = updated_task
                    print("Task updated successfully!")
                except IndexError:
                    print("Invalid task number.")
            else:
                print("No tasks to update.")
        elif choice == "4":
            if tasks:
                # Show complete to-do list and ask for task to mark complete
                print("\nSelect the task to mark as complete:")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")

                try:
                    task_index = int(input("Enter the number of the task to mark complete: ")) - 1
                    task_to_remove = tasks[task_index]
                    tasks.remove(task_to_remove)
                    print(f"Task '{task_to_remove}' marked as complete!")
                except IndexError:
                    print("Invalid task number.")
            else:
                print("No tasks to mark as complete.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

        # Ask if user wants to re-run
        run_again = input("Do you want to run the program again? (y/n): ").lower()
        if run_again != "y":
            break

todo_list()
