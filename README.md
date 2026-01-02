# Todo App CLI

A Python in-memory command-line interface (CLI) application for managing personal tasks. The application allows users to add, update, delete, view, and mark tasks as complete/incomplete with a clean, color-coded table view.

## Features

- **Add Task**: Create new tasks with titles and optional descriptions
- **Update Task**: Modify existing tasks by ID
- **Delete Task**: Remove tasks by ID
- **View Tasks**: Display all tasks in a formatted table with color-coded status
- **Mark Complete/Incomplete**: Toggle task completion status
- **Color-coded Status**: Green ✅ for completed tasks, Red ❌ for incomplete tasks
- **Table Format Display**: Organized view with ID, Title, Description, and Status columns
- **Input Validation**: Proper error handling for invalid inputs
- **In-Memory Storage**: All data stored in memory (lost on exit)

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup
The application requires no external dependencies - it uses only Python's standard library:

```bash
# Clone or download the repository
git clone <repository-url>

# Navigate to the project directory
cd todo-app-cli
```

## How to Run

Simply execute the Python script:

```bash
python todo_app.py
```

## Usage Examples

### Main Menu
When you run the application, you'll see the main menu:

```
==================================================
TODO APP CLI
==================================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit
--------------------------------------------------
```

### Adding a Task
```
--- Add New Task ---
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, bread, eggs
Task added successfully with ID: 550e8400-e29b-41d4-a716-446655440000...
```

### Viewing Tasks
Tasks are displayed in a formatted table:

```
--- All Tasks ---
ID          | Title              | Description                    | Status
----------+- --------------------+- ------------------------------+- -------------
550e8400... | Buy groceries      | Milk, bread, eggs              | ❌ Incomplete
a1b2c3d4... | Complete project   | Finish the CLI app             | ✅ Completed
```

### Updating a Task
```
--- Update Task ---
Enter task ID to update: 550e8400-e29b-41d4-a716-446655440000
Current title: Buy groceries
Enter new title (or press Enter to keep current): Buy groceries and cook dinner
Current description: Milk, bread, eggs
Enter new description (or press Enter to keep current): Milk, bread, eggs, chicken
Task updated successfully.
```

### Marking Task Complete/Incomplete
```
--- Mark Task Complete/Incomplete ---
Enter task ID: 550e8400-e29b-41d4-a716-446655440000
Current status: Incomplete
Mark as (1) Complete or (2) Incomplete? (1/2, or Enter to toggle): 1
Task marked as Completed.
```

## Table View & Colors

The application displays tasks in a clean table format with the following columns:
- **ID**: Unique identifier for each task (truncated for readability)
- **Title**: The main task title
- **Description**: Optional task details (or "(No description)" if empty)
- **Status**: Color-coded status indicator with text

### Color Coding
- **Green ✅ Completed**: Tasks that are marked as complete
- **Red ❌ Incomplete**: Tasks that are not yet complete

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Architecture

- **Single File**: Entire application in one Python file (`todo_app.py`)
- **In-Memory Storage**: All data stored in memory only (no persistence)
- **Standard Library Only**: No external dependencies required
- **CLI Interface**: Menu-driven command-line interface"# Ghouse-HackathonII-PhaseI" 
