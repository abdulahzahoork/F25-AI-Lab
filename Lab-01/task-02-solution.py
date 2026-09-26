# Mini Project: A dynamic To-Do list (add/remove/view items in a loop)

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Items")
    print("2. Add Items")
    print("3. Remove Items")
    print("4. Exit")

    
def view_items(todo_list):
    if not todo_list:
        print("Your list is empty.")
    else:
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")


def add_items(todo_list):
    item = input("Enter a new item: ")
    todo_list.append(item)
    print(f"{item} added!")


def remove_items(todo_list):
    view_items(todo_list)
    if todo_list:
        try:
            num = int(input("Enter the item number to remove: "))
            removed = todo_list.pop(num-1)
            print(f"{removed} removed!")
        except(ValueError, IndexError):
            print("Invalid item number.")



def main():
    todo_list = []

    while True: 
        show_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                view_items(todo_list)
            case "2":
                add_items(todo_list)
            case "3":
                remove_items(todo_list)
            case "4":
                print("Exiting program! Goodbye.")
                break
            case _:
                print("Please choose a valid option!")
        


main()