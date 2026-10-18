
def add_item(items, item):
    """Add an item to the list."""
    item = item.strip()

    if item:
        items.append(item)
        return True

    return False


def remove_item(items, item):
    """Remove an item if it exists."""
    if item in items:
        items.remove(item)
        return True

    return False


def display_items(items):
    """Display all items in the list."""
    if not items:
        print("Your list is empty.")
        return

    print("\nYour Items:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")
