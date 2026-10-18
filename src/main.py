
from src.utils import add_item, remove_item, display_items


def main():
    """Run the interactive item manager."""
    items = []

    while True:
        print("\n--- Item Manager ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Delete Item")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            item = input("Enter item to add: ")

            if add_item(items, item):
                print("Item added successfully.")
            else:
                print("Item cannot be empty.")

        elif choice == "2":
            display_items(items)

        elif choice == "3":
            item = input("Enter item to delete: ").strip()

            if remove_item(items, item):
                print("Item removed successfully.")
            else:
                print("Item not found.")

        elif choice == "4":
            print("Thank you for using Item Manager!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
