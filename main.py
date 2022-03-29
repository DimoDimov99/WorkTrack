from todo import todo_menu
from utils import *


def mark_goal():
    if user_input == "track":
        work_task_creation()
    elif user_input == "list":
        list_tasks()
    elif user_input == "time":
        current_time()
    elif user_input == "clear":
        clear()
    elif user_input == "save":
        save_info()
    elif user_input == "commands":
        print_commands()
    elif user_input == "hours check":
        print_found_hours()
    elif user_input == "todo":
        todo_menu()
    else:
        print("Invalid input")


if __name__ == "__main__":
    print("Welcome to WorkTrack!")
    print(f"To see all available commands, type 'commands'!")
    user_input = input("Choose a command to begin: ").lower()
    while user_input != "quit":
        mark_goal()
        user_input = input("Choose a command to begin: ").lower()
    print("Quiting the app...")
