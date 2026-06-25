# main.py
tasks = []

def add_task():
    print("\n--- Add a New Task ---")
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (e.g., 2026-07-01): ")
    
    task = {
        "name": name,
        "description": description,
        "deadline": deadline
    }
    tasks.append(task)
    print(f"✅ Task '{name}' added successfully!")

def view_all_tasks():
    print("\n--- All Tasks ---")
    if not tasks:
        print("No tasks available.")
        return
    # Shows a list of names and deadlines as requested
    for task in tasks:
        print(f"📌 Name: {task['name']} | 📅 Deadline: {task['deadline']}")

if __name__ == "__main__":
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
