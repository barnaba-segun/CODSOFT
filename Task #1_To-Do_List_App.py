import json  # Import the json module to handle JSON data

def add_tasks(tasks):
    """Add a new task to the list."""
    task_id = len(tasks) + 1  # Generate a new task ID
    title = input("Enter task title: ")  # Prompt user for task title
    tasks.append({'id': task_id, 'title': title, 'is_completed': False})  # Add task to the list
    print('Task added successfully')

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print('No tasks available')  # Inform user if no tasks are available
        return
    for task in tasks:
        status = '✔️  Completed' if task['is_completed'] else '❌  Incomplete'  # Determine task status
        print(f"{task['id']}. {task['title']} - {status}")  # Print task details

def update_task(tasks):
    """Update or check off an existing task."""
    task_id = int(input("Enter the task ID to update or check off: "))  # Prompt user for task ID
    for task in tasks:
        if task['id'] == task_id:
            print(f'Current Task: {task["title"]}')  # Display current task title
            new_title = input('Enter new task title (leave blank to keep current title): ')  # Prompt for new title
            if new_title:
                task['title'] = new_title  # Update task title if provided
            task['is_completed'] = input('Mark as completed? (yes/no): ').lower() == 'yes'  # Update completion status
            print('✔️  Task updated successfully')
            return
    print('Task not found')  # Inform user if task ID is not found

def delete_task(tasks):
    """Delete a task from the list."""
    task_id = int(input('Enter the task ID to delete: '))  # Prompt user for task ID
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)  # Remove task from the list
            print('Task deleted successfully')
            return
    print('Task not found')  # Inform user if task ID is not found

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)  # Write tasks to file
    print('Tasks saved successfully')

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)  # Read tasks from file
    except FileNotFoundError:
        tasks = []  # Initialize empty list if file not found
    return tasks

def main():
    """Main function to run the to-do list app."""
    tasks = load_tasks()  # Load tasks from file
    
    while True:
        # Display menu options
        print('\n--- To-Do List App Menu ---')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Update & Check off Task')
        print('4. Delete Task')
        print('5. Save Tasks and Exit')
        choice = input('\nChoose an option: ')  # Prompt user for menu choice
        
        if choice == '1':
            add_tasks(tasks)  # Add a new task
        elif choice == '2':
            view_tasks(tasks)  # View all tasks
        elif choice == '3':
            update_task(tasks)  # Update an existing task
        elif choice == '4':
            delete_task(tasks)  # Delete a task
        elif choice == '5':
            save_tasks(tasks)  # Save tasks to file and exit
            print('Exiting...Exited successfully!')
            break
        else:
            print('Invalid choice. Please try again.')  # Handle invalid menu choice

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly
