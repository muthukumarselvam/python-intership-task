tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        item = input("What needs to be done? ")
        tasks.append(item)
        print("Task added.")
    elif choice == '2':
        print("\nYour Tasks:")
        for index, t in enumerate(tasks, start=1):
            print(f"{index}. {t}")
    elif choice == '3':
        for index, t in enumerate(tasks, start=1):
            print(f"{index}. {t}")
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    elif choice == '4':
        print("Goodbye!")
        break