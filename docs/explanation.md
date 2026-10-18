# Explanation of Python List Operations

## Introduction
The Item Manager demonstrates Python functions and list manipulation.

## Functions
- `add_item(items, item)`: Adds a non-empty item using `append()`.
- `remove_item(items, item)`: Checks whether an item exists and removes it using `remove()`.
- `display_items(items)`: Displays the list using a `for` loop and `enumerate()`.
- `main()`: Runs the interactive menu until the user exits.

## List Operations
- `append()` adds an item to the end of a list.
- `remove()` deletes the first matching item.
- `enumerate()` provides an index and item while looping.
- `if` and `else` handle decisions.
- `while True` repeats the menu.

## Error Handling
The application handles empty item input, attempts to delete missing items, empty lists, and invalid menu choices.

## Sample Run
```text
--- Item Manager ---
1. Add Item
2. View Items
3. Delete Item
4. Exit
Enter your choice: 1
Enter item to add: Book
Item added successfully.
```

## Testing
Unit tests verify adding items, rejecting empty input, removing existing items, and handling missing items.