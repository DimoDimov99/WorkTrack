import sqlite3
from datetime import datetime

from utils import current_time


def create_todo_table():
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS todos(todo_name text primary key, current_day text, current_time text, finished integer, time_stamp text)")

    connection.commit()
    connection.close()


def get_all_todos():
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM todos")
    # [(name, author, read), (name, author, read)]
    todo = [{"todo_name": row[0], "current_day": row[1], "current_time": row[2], "finished": row[3], "time_stamp": row[4]}
            for row in cursor.fetchall()]
    connection.close()
    return todo


def mark_todo_finished():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    user_input = input(
        "Enter the name of the todo you want to mark as finished: ")
    check = cursor.execute(
        "SELECT * FROM todos WHERE todo_name=?", (user_input,))
    is_in_todos = list(check)
    if is_in_todos:
        print(f"The todo [{user_input}] is found! Updating its status!")
        cursor.execute(
            f"UPDATE todos SET finished='1' WHERE todo_name=?", (
                user_input,))
        cursor.execute(f"UPDATE todos SET time_stamp=?", (current_time,))
    else:
        print(
            f"Sorry, the provided todo [{user_input}] is not present in the todos, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def mark_todo_not_finished():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    user_input = input(
        "Enter the name of the todo you want to mark as unfinished: ")
    check = cursor.execute(
        "SELECT * FROM todos WHERE todo_name=?", (user_input,))
    is_in_todos = list(check)
    if is_in_todos:
        print(f"The todo [{user_input}] is found! Updating its status!")
        cursor.execute(
            "UPDATE todos SET finished='0' WHERE todo_name=?", (user_input,))
        cursor.execute(f"UPDATE todos SET time_stamp=?", (current_time,))
    else:
        print(
            f"Sorry, the provided todo [{user_input}] is not present in the todos, double check!")
    test_input = input("Resolve the program? : (Y): ")
    connection.commit()
    connection.close()


def insert_todo(todo_name):
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    current_day = datetime.now().strftime("%A")
    # ",0); DROP TABLE books;
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    try:
        # time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        cursor.execute("INSERT INTO todos VALUES(?, ?, ?, 0, ?)",
                       (todo_name, current_day, current_time, ""))
        print("The todo is successfully added!")
    except sqlite3.IntegrityError:
        print(f"The todo {todo_name} already exist!")
    connection.commit()
    connection.close


def delete_todo(name):
    connection = sqlite3.connect("todo_data.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todos WHERE todo_name=?", (name,))
    connection.commit()
    connection.close()
