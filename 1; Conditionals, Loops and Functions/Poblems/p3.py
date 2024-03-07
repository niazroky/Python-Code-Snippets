shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} added to shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from shopping list.")
    else:
        print(f"{item} not found in shopping list.")

def view_list():
    if len(shopping_list) == 0:
        print("Shopping list is empty.")
    else:
        print("Shopping list:")
        for item in shopping_list:
            print(item)

while True:
    print("Select an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Quit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        item = input("Enter item: ")
        add_item(item)
    elif choice == 2:
        item = input("Enter item: ")
        remove_item(item)
    elif choice == 3:
        view_list()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")

        