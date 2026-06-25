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
    for task in tasks:
        print(f"📌 Name: {task['name']} | 📅 Deadline: {task['deadline']}")

def view_individual_task():
    print("\n--- View Individual Task ---")
    if not tasks:
        print("No tasks available.")
        return
    
    search_name = input("Enter the task name to view details: ")
    for task in tasks:
        if task['name'].lower() == search_name.lower():
            print(f"\n📌 Name: {task['name']}")
            print(f"📝 Description: {task['description']}")
            print(f"📅 Deadline: {task['deadline']}")
            return
    print("❌ Task not found.")

if __name__ == "__main__":
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Individual Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_all_tasks()
        elif choice == "3":
            view_individual_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
