def main():
    tasks = []

    while True:
        print("MENU")
        print("1. ADD TASKS")
        print("2. SHOW TASKS")
        print("3. MARK AS COMPLETE")
        print("4. EXIT")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("How many new tasks do you have to add: "))

            for _ in range(n):
                task_name = input("Enter the task: ")
                tasks.append({"task": task_name, "done": False})
                print("Task added!")

        elif choice == 2:
            print("\nTasks:")
            for task in tasks:
                print(f"{task['task']} - {'Done' if task['done'] else 'Not done'}")

        elif choice == 3:
            task_name = input("Enter the task to mark as complete: ")
            for task in tasks:
                if task['task'] == task_name:
                    task['done'] = True
                    print("Task marked as complete.")
                    break
            else:
                print("Task not found.")

        elif choice == 4:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()


