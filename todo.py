from database import db
from utils import clear
import time


USER_CHOICE = """
Enter:
- 'add' to add a new todo
- 'list' to list all todo/s
- 'done' to mark a todo as done
- 'not finished' to mark a todo as not finished yet
- 'delete' to delete a todo
- 'quit' to quit
Your choice: """


def todo_menu():
    clear()
    db.create_todo_table()
    user_input = input(USER_CHOICE)
    while user_input != 'quit':
        if user_input == 'add':
            clear()
            insert_todo()
        elif user_input == 'list':
            clear()
            list_todos()
        elif user_input == 'done':
            clear()
            db.mark_todo_finished()
        elif user_input == 'not finished':
            clear()
            db.mark_todo_not_finished()
        elif user_input == 'delete':
            clear()
            prompt_delete_todo()
        user_input = input(USER_CHOICE)
    if user_input == "quit":
        print("[Quitting the todo app and resolving to main screen...]")
        print("\n")


def insert_todo():
    todo_name = input("Enter Todo: ")
    db.insert_todo(todo_name)
    # Stupid but good fix for now
    test_input = input("Resolve the program? : (Y): ")


def list_todos():
    clear()
    for todo in db.get_all_todos():
        # book[3] will be a falsy value (0) if not read
        finished = 'Done' if todo['finished'] else 'Not done'
        print("\n")
        print(
            f"[Todo]: {todo['todo_name']} [Day]: {todo['current_day']} [CREATED]: {todo['current_time']} — Status: {finished} [LAST UPDATED] [{todo['time_stamp']}]")
        print(50 * "-")
    time.sleep(0.6)
    # Stupid but good fix for now
    test_input = input("Resolve the program? : (Y): ")


def prompt_delete_todo():
    name = input('Enter the name of the todo you wish to delete: ')
    db.delete_todo(name)
    print(f"The todo: [{name}] is succesfuly deleted!")
    # Stupid but good fix for now
    test_input = input("Resolve the program? : (Y): ")
