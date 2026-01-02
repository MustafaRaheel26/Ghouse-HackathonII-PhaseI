# Data Model: Todo App CLI

## Task Entity

### Attributes
- **id** (string/integer): Unique identifier for the task
  - Auto-generated when task is created
  - Used for identifying tasks in operations (update, delete, mark complete)

- **title** (string): Required task title
  - Cannot be empty
  - User-defined text describing the task

- **description** (string): Optional task description
  - Can be empty or null
  - User-defined additional details about the task

- **completed** (boolean): Task completion status
  - Default: False (incomplete)
  - Can be toggled between True (complete) and False (incomplete)

### Constraints
- id: Must be unique within the application session
- title: Required field, cannot be empty or None
- completed: Boolean value only (True/False)

### Example Representation
```python
{
    "id": "1",
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": False
}
```

## In-Memory Storage Structure

### Task Collection
Tasks will be stored in a Python list:
```python
tasks = [
    {
        "id": "1",
        "title": "Buy groceries",
        "description": "Milk, bread, eggs",
        "completed": False
    },
    {
        "id": "2",
        "title": "Walk the dog",
        "description": "",
        "completed": True
    }
]
```

### ID Generation
- Use a simple incrementing counter starting from 1
- Convert to string for consistency
- Ensure uniqueness by checking against existing IDs

## Data Operations
- Add: Append new task object to the list
- Update: Find task by ID and modify its attributes
- Delete: Remove task object from the list by ID
- View: Iterate through the list and display all tasks
- Mark Complete/Incomplete: Find task by ID and toggle the completed status