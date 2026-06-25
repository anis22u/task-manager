# main.py
tasks = []

def add_task():
    print("\n--- Add a New Task ---")
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (e.g., 2026-07-01): ")
    
    # Store the task as a dictionary
    task = {
        "name": name,
        "description": description,
        "deadline": deadline
    }
    
    tasks.append(task)
    print(f"✅ Task '{name}' added successfully!")

# Simple test loop
if __name__ == "__main__":
    while True:
        add_task()
        again = input("\nDo you want to add another task? (y/n): ")
        if again.lower() != 'y':
            break
