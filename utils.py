import os
from time_handler import time_to_num, display_time
from datetime import date, datetime
import time
import sys

HOME_PATH = os.getcwd()  # get user main directory path

commands = {
    "track": "begin to track an activity",
    "list": "list the content of selected txt file",
    "time": "print current time in the console",
    "clear": "clear output in the terminal",
    "save": "save all content from txt file inside full_info.txt in the respective directory",
    "quit": "quit the application",
    "hours check": "list how much work is done for a specific day",
    "todo": "trigger todo app menu"
}


def clear() -> None:
    """Clears the input into the terminal"""
    os.system("clear")


def display_txt_files() -> None:
    # most likely will need to refactor in some point of time
    # It will quit the application if for example we use hours check in an empty directory, because there is nothing to check!
    """Function to display all txt files inside the current directory"""
    txt_files = []
    for x in os.listdir():
        if x.endswith(".txt"):
            txt_files.append(x)
    if len(txt_files) > 0:
        print("All txt files:")
        for txt in txt_files:
            print(txt)
    # if len(txt_files) == 0:
    #     print(f"No txt files in directory {os.getcwd()}")
    #     print("Exiting the program now!")
    #     exit(-1)


def display_work_directory_txt_files() -> None:
    # cheap fix for now, to not quit when new working directory is generated for the current day
    """Function to display all txt files inside the current directory"""
    txt_files = []
    for x in os.listdir():
        if x.endswith(".txt"):
            txt_files.append(x)
    if len(txt_files) > 0:
        print("All txt files:")
        for txt in txt_files:
            print(txt)
    # if len(txt_files) == 0:
    #     print(f"No txt files in directory {os.getcwd()}")


def list_all_dirs() -> None:
    """Function to display all directories inside the current directory"""
    folder = os.getcwd()
    subfolders = [f.name for f in os.scandir(folder) if f.is_dir()]
    # clear()
    print("\n")
    print("All directories: ")
    for folders in subfolders:
        print(folders)


def display_working_dir() -> None:
    """Displaying current working directory"""
    print(f"current working directory is: {os.getcwd()}")


def work_task_track() -> None:  # helper function now!
    """This function writes to a given .txt file the tasks that we are working on"""
    clear()
    display_work_directory_txt_files()
    text_file_name = datetime.today().strftime("%A")
    text_file_name += "_work_done.txt"  # extension
    current_day = datetime.now().strftime("%A")
    current_day_of_month = datetime.now().strftime("%B")
    current_month = datetime.now().strftime("%d")
    work_beginning = input("Beginning of the work day (Y/N)?: ")
    if work_beginning.lower() == "y":
        delimiter()
    elif work_beginning.lower() == "n":
        print("Delimiter not addded!")
    else:
        print("Invalid input, please double check!")
        return -1
    user_input = input("Please enter the task you are working on: ")
    project = input("Does you know the project for the task? (Y/N): ")
    if project.lower() == "y":
        work_project = input("Enter the name of the project: ")
        project = work_project
    elif project.lower() == "n":
        project = " "
    else:
        project = ""  # instead of handling errors, return empty string from input different from y
    activity_begin = input(f"Begin the task: [{user_input}]: Y/N ? : ")
    if activity_begin.lower() == "y":
        begin_time = datetime.now().strftime('%H:%M:%S')
        begin_time_int = time_to_num(begin_time)
        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"Current Day: {current_day} [{current_day_of_month} {current_month}]\nPROJECT: [{project}] | CURRENT_TASK -> [{user_input}] is started at: [{datetime.now().strftime('%B %d %Y %H:%M:%S')}]\n")
            file.write(40 * "-")
            file.write("\n")
        activity_end = input(
            f"Done with the current task [{user_input}]: Y/N ? : ")
    elif activity_begin.lower() == "n":
        print(f"Task [ {user_input} ] aborted!")
        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"Current Day: {current_day} [{current_day_of_month} {current_month}]\nPROJECT: [{project}] | CURRENT_TASK -> [{user_input}] is aborted at: [{datetime.now().strftime('%B %d %Y %H:%M:%S')}]")
            file.write("\n")
            file.write(40 * "-")
            file.write("\n")
        return -1
    elif activity_begin.lower() != "n" and activity_begin.lower() != "y":
        print("Invalid input, please double check!")
        return -1
    if activity_end.lower() == "y":
        end_time = datetime.now().strftime('%H:%M:%S')
        end_time_int = time_to_num(end_time)
        result = end_time_int - begin_time_int
        print(f"Task finished! It took you: [ {display_time(result)} ]")

        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"Current Day: {current_day} [{current_day_of_month} {current_month}]\nPROJECT: [{project}] | CURRENT_TASK -> [{user_input}] is finished at: [FINISHED {datetime.now().strftime('%B %d %Y %H:%M:%S')}] it took you: [{display_time(result)}]")
            file.write("\n")
            file.write(40 * "-")
            file.write("\n")
    elif activity_end.lower() == "n":
        print(f"Task [ {user_input} ] aborted!")
        with open(text_file_name, "a", encoding="utf8") as file:
            file.write(
                f"Current Day: {current_day} [{current_day_of_month} {current_month}]\nPROJECT: [{project}] | CURRENT_TASK -> [{user_input}] is aborted at: [{datetime.now().strftime('%B %d %Y %H:%M:%S')}]")
            file.write("\n")
            file.write(40 * "-")
            file.write("\n")
    elif activity_end.lower() != "y" and activity_end.lower() != "n":
        print("Invalid input, please double check!")
        return -1
    work_ending = input("End of the workday (Y/N)?: ")
    if work_ending.lower() == "y":
        delimiter()
    elif work_ending.lower() == "n":
        print("Delimiter not addded!")
    else:
        print("Invalid input, please double check!")
        return -1

#************************#
#   deprecate function
#************************#
# def create_work_directory() -> None:
#     """This function create a new directory"""
#     default_path = os.getcwd()  # better naming
#     if default_path != HOME_PATH:
#         os.chdir(HOME_PATH)
#     list_all_dirs()
#     current_exist_path = os.getcwd()
#     print("\n")
#     user_input = input("Enter the directory name: ")
#     dir_name = user_input
#     directory_path = os.getcwd()
#     check_existing = os.path.join(directory_path, dir_name)
#     # print(current_exist_path)
#     # print(check_existing)
#     check = os.path.exists(check_existing)
#     if check:
#         print(f"Sorry, the directory {dir_name} already exist!")
#         return -1
#     else:
#         try:
#             os.makedirs(dir_name, exist_ok=True)
#             print(f"Directory {dir_name} is created succesfully!")
#         except OSError as error:
#             print(f"Directory {dir_name} already exist!")


def work_task_creation() -> None:
    """This function invokes work_task_track() and it's the core function of the program.
    Log and write the work tasks that we are doing to a .txt file"""  # main track function
    current_path = os.getcwd()
    print(current_path)
    if current_path != HOME_PATH:
        os.chdir(HOME_PATH)
        current_path = HOME_PATH
    current_day = datetime.today().strftime("%A")
    destination_path = f"{current_path}/{current_day}"
    if current_day and os.path.exists(destination_path):
        os.chdir(destination_path)
        print(f"Switched to {current_day} dir!")
        work_task_track()
    else:
        print(f"{current_day} directory is missing!!! Creating now....")
        os.makedirs(destination_path)
        os.chdir(destination_path)
        work_task_track()


def list_tasks() -> None:
    """Listing all tasks in .txt file in certain directory"""
    default_path = os.getcwd()
    if default_path != HOME_PATH:
        os.chdir(HOME_PATH)
    clear()
    # list_all_txt()
    list_all_dirs()
    print("\n")
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        working_dir = os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    clear()
    display_working_dir()
    display_txt_files()
    txt_input = input("Which txt file would you like to list: ")
    txt_input += ".txt"
    try:
        print("\n")
        with open(txt_input, "rt", encoding="utf8") as task_file:
            lines = task_file.readlines()
            if len(lines) == 0:
                print("The file is empty")
                print()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"Looks like the file {txt_input} does not exist!")


def current_time() -> None:
    """Output current month, day, year and time to the terminal"""
    splitter = "*" * 50
    clear()
    time_now = datetime.now().strftime('%B %d %Y %H:%M:%S')
    print(splitter)
    print()
    print(time_now)
    print()
    print(splitter)
    time.sleep(0.6)


def save_info() -> None:
    """Saves the content of a given .txt file to a txt file"""
    default_path = os.getcwd()
    if default_path != HOME_PATH:
        os.chdir(HOME_PATH)
    clear()
    # list_all_txt()
    list_all_dirs()
    print("\n")
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.title()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        working_dir = os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    display_txt_files()
    filename = input(
        "Enter the filename that you want to get and save the information: ")
    filename += ".txt"

    try:
        with open(filename, "r", encoding="utf8") as file:
            with open("full-info.txt", "a", encoding="utf8") as saved_info:
                for line in file:
                    saved_info.write(line)
            print(
                f"Successfully saved the content of {filename} into full-info.txt! inside: {os.getcwd()}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist!")


def print_found_hours() -> None:
    """Print the tasks done for given Month/Day"""
    default_path = os.getcwd()  # better naming
    if default_path != HOME_PATH:
        os.chdir(HOME_PATH)
    clear()
    display_working_dir()
    # list_all_txt()
    list_all_dirs()
    print("\n")
    current_dir = os.getcwd()
    target_dir = ""
    custom_dir = input("Enter the name of the directory: ")
    custom_dir = custom_dir.capitalize()
    target_dir += f"{current_dir}/{custom_dir}"
    if os.path.isdir(f"{custom_dir}"):
        working_dir = os.chdir(target_dir)
    else:
        print(f"The directory {custom_dir} does not exist!")
        return -1
    clear()
    display_working_dir()
    display_txt_files()
    check_phrase_month = input("For which month do you want to check?: ")
    check_phrase_day = input("For which day do you want to check?: ")
    # check_phrase_year to implement

    phrase = f"FINISHED {check_phrase_month.capitalize()} {check_phrase_day}"
    # print(phrase)
    filename = input("Enter the filename you need to check working hours: ")
    filename += ".txt"
    info = []
    if os.path.isfile(f"{filename}"):
        """Print the lines in the file that contains the given phrase."""
        with open(filename, "r") as file:
            clear()
            for line in file:
                if phrase in line:
                    print(line.replace("\n", ""))
                    info.append(line)
                    print(100 * "-")
            prompt = input("Do you want to save this information (Y/N)?: ")
            if prompt.lower() == "y":
                location = os.getcwd()
                os.chdir(location)
                with open("tasks-completed.txt", "a", encoding="utf8") as file:
                    for i in info:
                        file.write(i)
                        file.write("*" * 100)
                        file.write("\n")
            else:
                print("Information not saved!")
    else:
        print(f"The file {filename} does not exist!")
        return -1


def delimiter():
    display_working_dir()
    text_file_name = datetime.today().strftime("%A")
    text_file_name += "_work_done.txt"  # extension
    current_day = datetime.now().strftime("%A")
    current_day_of_month = datetime.now().strftime("%B")
    current_month = datetime.now().strftime("%d")
    current_year = datetime.now().strftime("%Y")
    with open(text_file_name, "a", encoding="utf8") as file:
        file.write("\n")
        file.write(
            f"{current_day} [{current_day_of_month} {current_month} {current_year}]".center(100, "="))
        file.write("\n")
        print("Delimiter added!")


def print_commands() -> None:
    """Print all available commands"""
    clear()
    print(40 * "*")
    for key, value in commands.items():
        print(f"{key} -> {value}\n")
    print(40 * "*")
