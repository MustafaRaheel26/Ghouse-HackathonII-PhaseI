# Quickstart Guide: Todo App CLI

## Overview
A simple command-line interface (CLI) application for managing personal tasks. The application runs entirely in memory and does not persist data between sessions.

## Prerequisites
- Python 3.8 or higher
- No external dependencies required

## Getting Started

### 1. Running the Application
```bash
python todo_app.py
```

### 2. Main Menu Options
Once the application starts, you will see the main menu with the following options:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

### 3. Using the Application

#### Adding a Task
1. Select "Add Task" from the main menu
2. Enter a title for the task (required)
3. Optionally enter a description (press Enter to skip)
4. The task will be added with a unique ID and marked as incomplete

#### Viewing Tasks
1. Select "View All Tasks" from the main menu
2. All tasks will be displayed with their ID, title, description, and completion status

#### Updating a Task
1. Select "Update Task" from the main menu
2. Enter the ID of the task you want to update
3. Enter the new title (or press Enter to keep the current title)
4. Enter the new description (or press Enter to keep the current description)

#### Deleting a Task
1. Select "Delete Task" from the main menu
2. Enter the ID of the task you want to delete
3. Confirm the deletion

#### Marking Task Complete/Incomplete
1. Select "Mark Task Complete/Incomplete" from the main menu
2. Enter the ID of the task you want to update
3. The completion status will be toggled

### 4. Important Notes
- All data is stored in memory only and will be lost when the application exits
- Task IDs are automatically generated and unique within the session
- Invalid inputs will be handled gracefully with error messages
- The application will continue running until you select "Exit" from the main menu