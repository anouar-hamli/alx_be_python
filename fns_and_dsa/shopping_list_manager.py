import os
import sys

file_path = __file__
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    print("Error: File does not exist or is empty.")
    sys.exit(1)


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Check 3: Implementation of an array shopping_list
    shopping_list = []

    while True:
        # Check 4: Calling display_menu function
        display_menu()

        try:

            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("Shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
