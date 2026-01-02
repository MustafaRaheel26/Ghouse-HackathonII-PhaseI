#!/usr/bin/env python3
"""
Todo App CLI - A Python in-memory CLI Todo application

This application allows users to add, update, delete, view, and mark tasks complete/incomplete.
All data is stored in memory only and will be lost when the application exits.
By Mustafa (71798)
"""

import uuid
from typing import List, Dict, Optional


# ANSI color codes
class Colors:
    GREEN = '\033[92m'  # Green for completed tasks
    RED = '\033[91m'     # Red for incomplete tasks
    RESET = '\033[0m'    # Reset to default color
    BOLD = '\033[1m'     # Bold text
    UNDERLINE = '\033[4m' # Underline


class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id (str): Unique identifier for the task
        title (str): Required task title
        description (str): Optional task description
        completed (bool): Task completion status (default: False)
    """

    def __init__(self, task_id: str, title: str, description: str = "", completed: bool = False):
        """
        Initialize a new Task instance.

        Args:
            task_id (str): Unique identifier for the task
            title (str): Required task title
            description (str): Optional task description
            completed (bool): Task completion status (default: False)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self) -> str:
        """
        Return a string representation of the task.

        Returns:
            str: Formatted string with task details
        """
        colored_status = self.get_colored_status()
        status_text = self.get_status_text()
        return f"[{colored_status}] {self.id}: {self.title} - {self.description if self.description else '(No description)'} ({status_text})"

    def get_colored_status(self) -> str:
        """
        Return a colored status symbol for the task.

        Returns:
            str: Colored status symbol (green checkmark for completed, red for incomplete)
        """
        if self.completed:
            return f"{Colors.GREEN}✅{Colors.RESET}"
        else:
            return f"{Colors.RED}❌{Colors.RESET}"

    def get_status_text(self) -> str:
        """
        Return the status as text.

        Returns:
            str: 'Completed' if task is completed, 'Incomplete' otherwise
        """
        return "Completed" if self.completed else "Incomplete"


class TaskManager:
    """
    Manages all tasks in the application.

    Handles adding, updating, deleting, viewing, and marking tasks complete/incomplete.
    """

    def __init__(self):
        """
        Initialize a new TaskManager instance with an empty task list.
        """
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the task list.

        Args:
            title (str): Required task title
            description (str): Optional task description

        Returns:
            Task: The newly created task
        """
        # Generate a unique ID for the new task
        task_id = str(uuid.uuid4())
        task = Task(task_id, title, description, False)
        self.tasks.append(task)
        return task

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task by its ID.

        Args:
            task_id (str): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if task was found and updated, False otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (str): ID of the task to delete

        Returns:
            bool: True if task was found and deleted, False otherwise
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return True
        return False

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.

        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks

    def mark_task_complete(self, task_id: str, completed: bool = True) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id (str): ID of the task to update
            completed (bool): Whether the task should be marked as completed

        Returns:
            bool: True if task was found and updated, False otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = completed
                return True
        return False

    def toggle_task_completion(self, task_id: str) -> bool:
        """
        Toggle a task's completion status.

        Args:
            task_id (str): ID of the task to toggle

        Returns:
            bool: True if task was found and toggled, False otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                return True
        return False


class CLI:
    """
    Command Line Interface for the Todo application.

    Handles user input, menu display, and interaction with the TaskManager.
    """

    def __init__(self):
        """
        Initialize the CLI with a TaskManager instance.
        """
        self.task_manager = TaskManager()

    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*50)
        print("TODO APP CLI")
        print("="*50)
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get and validate user menu choice.

        Returns:
            str: Valid user choice (1-6)
        """
        while True:
            choice = input("Enter your choice (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def add_task(self):
        """
        Handle adding a new task.
        """
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()

        task = self.task_manager.add_task(title, description)
        print(f"Task added successfully with ID: {task.id[:8]}...")  # Show shortened ID

    def view_tasks(self):
        """
        Handle viewing all tasks in a table format with colors.
        """
        print("\n--- All Tasks ---")
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        # Calculate column widths for proper alignment
        id_width = max(10, len("ID"))  # At least 10 characters for ID
        title_width = max(20, len("Title"))  # At least 20 characters for Title
        desc_width = max(30, len("Description"))  # At least 30 characters for Description
        status_width = max(12, len("Status"))  # At least 12 characters for Status

        # Check if we need to adjust widths based on actual content
        for task in tasks:
            id_width = max(id_width, len(task.id[:8] + "..."))
            title_width = max(title_width, len(task.title))
            if task.description:
                desc_width = max(desc_width, len(task.description))

        # Create table header with underlines
        header = f"{Colors.BOLD}{'ID':<{id_width}} | {'Title':<{title_width}} | {'Description':<{desc_width}} | {'Status':<{status_width}}{Colors.RESET}"
        separator = f"{'-' * id_width}-+-{'-' * title_width}-+-{'-' * desc_width}-+-{'-' * status_width}"

        print(header)
        print(separator)

        # Print each task in table format
        for task in tasks:
            shortened_id = task.id[:8] + "..."
            title = task.title
            description = task.description if task.description else "(No description)"
            colored_status = task.get_colored_status()
            status_text = task.get_status_text()

            # Truncate long text if needed
            if len(title) > title_width:
                title = title[:title_width-3] + "..."
            if len(description) > desc_width:
                description = description[:desc_width-3] + "..."

            # Print the row with colors
            print(f"{shortened_id:<{id_width}} | {title:<{title_width}} | {description:<{desc_width}} | {colored_status} {status_text}")

    def update_task(self):
        """
        Handle updating an existing task.
        """
        print("\n--- Update Task ---")
        task_id = input("Enter task ID to update: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty.")
            return

        # Find the task to show current values
        task_to_update = None
        for task in self.task_manager.get_all_tasks():
            if task.id.startswith(task_id) or task.id == task_id:
                task_to_update = task
                break

        if not task_to_update:
            print(f"Error: Task with ID '{task_id}' not found.")
            return

        print(f"Current title: {task_to_update.title}")
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        new_title = new_title if new_title else None

        print(f"Current description: {task_to_update.description}")
        new_description = input("Enter new description (or press Enter to keep current): ").strip()
        new_description = new_description if new_description else None

        # Only update if user provided new values
        if new_title is not None or new_description is not None:
            updated = self.task_manager.update_task(task_to_update.id, new_title, new_description)
            if updated:
                print("Task updated successfully.")
            else:
                print("Error: Could not update task.")
        else:
            print("No changes made.")

    def delete_task(self):
        """
        Handle deleting a task.
        """
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID to delete: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty.")
            return

        # Find the task
        task_to_delete = None
        for task in self.task_manager.get_all_tasks():
            if task.id.startswith(task_id) or task.id == task_id:
                task_to_delete = task
                break

        if not task_to_delete:
            print(f"Error: Task with ID '{task_id}' not found.")
            return

        print(f"Task to delete: {task_to_delete}")
        confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()

        if confirm in ['y', 'yes']:
            deleted = self.task_manager.delete_task(task_to_delete.id)
            if deleted:
                print("Task deleted successfully.")
            else:
                print("Error: Could not delete task.")
        else:
            print("Deletion cancelled.")

    def mark_task_completion(self):
        """
        Handle marking a task as complete/incomplete.
        """
        print("\n--- Mark Task Complete/Incomplete ---")
        task_id = input("Enter task ID: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty.")
            return

        # Find the task
        task_to_toggle = None
        for task in self.task_manager.get_all_tasks():
            if task.id.startswith(task_id) or task.id == task_id:
                task_to_toggle = task
                break

        if not task_to_toggle:
            print(f"Error: Task with ID '{task_id}' not found.")
            return

        print(f"Current status: {'Completed' if task_to_toggle.completed else 'Incomplete'}")
        new_status = input("Mark as (1) Complete or (2) Incomplete? (1/2, or Enter to toggle): ").strip()

        if new_status == '1':
            updated = self.task_manager.mark_task_complete(task_to_toggle.id, True)
        elif new_status == '2':
            updated = self.task_manager.mark_task_complete(task_to_toggle.id, False)
        elif new_status == '':
            updated = self.task_manager.toggle_task_completion(task_to_toggle.id)
        else:
            print("Invalid choice. Toggling status.")
            updated = self.task_manager.toggle_task_completion(task_to_toggle.id)

        if updated:
            new_status = "Completed" if task_to_toggle.completed else "Incomplete"
            print(f"Task marked as {new_status}.")
        else:
            print("Error: Could not update task status.")

    def run(self):
        """
        Main application loop that runs the CLI interface.
        """
        print("Welcome to the Todo App CLI!")
        print("All data is stored in memory only and will be lost when the application exits.")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_completion()
            elif choice == '6':
                print("\nThank you for using Todo App CLI. Goodbye!")
                break

            # Pause to let user see the result before showing the menu again
            input("\nPress Enter to continue...")


def main():
    """
    Main function to run the Todo App CLI.
    """
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()