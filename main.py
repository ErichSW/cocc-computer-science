# CS161 - Erich, Elijah, and Erika extra credit group project
# Goals are to view, search, edit, and save an external database

# get csv module for interfacing with the external CSV database
import csv
# get pandas for easy data manipulation
import pandas as pd
# set location of database
file_path = 'DBEC.csv'

# setting up functions here
def helps():
    print("all    = Display entire database.")
    print("search = Return a row containing a specific line of text.")
    print("add    = Enter a new row of data into the database.")
    print("delete = Remove a row of data from the database.")
    print("exit   = Close the program.")


def sheet():
    pd.set_option('display.width', None)
    df = pd.read_csv(file_path)
    print(df)


def search(file_path, search_term):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader, None)
        for row in csv_reader:
            if search_term in row:
                return row
    return None


def new_search():
    i = 0
    while i == 0:
        print("Enter search term, or 'exit'.")
        search_term = input()
        if search_term == "exit":
            i = 1
        else:
            result = search(file_path, search_term)
            if result:
                print(f"Found: {result}")
            else:
                print("Search term not found.")


def add_record():
    print("Type Course Number (5 digits):")
    course = input()[:5]  # limits no. of characters to 5, etc.
    course = str(course)  # makes sure input is always a string
    print("Type Course Name:")
    name = input()[:30]
    name = str(name)
    print("Type Number of Credits:")
    credit = input()[:1]
    credit = str(credit)
    print("Type Department Abbreviation (4 letters:")
    dept = input()[:4]
    dept = str(dept)
    dept = dept.upper()  # makes abbreviation all caps
    print("Type Description (max 100 char):")
    desc = input()[:100]
    desc = str(desc)
    print(course, name, credit, dept, desc)
    new_record = {course, name, credit, dept, desc}
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_record)

    # displays completed save
    pd.set_option('display.width', None)
    df = pd.read_csv(file_path)
    print(df)
    print("Success!")

    # df = pd.read_csv('DBEC.csv') # pull up CSV into python to work on data
    # df = df.write(new_record, ignore_index=True)
    # print(df)
    # df.to_csv('DBEC.csv', index=False) # save data back into csv when completed


def del_record():
    print("unfinished")


# main loop
d = 0
while d == 0:
    print("Enter command, or 'help'.")
    cmd = input()
    cmd = cmd.lower()
    # summon list of commands
    if cmd == "help":
        helps()
    # show whole sheet
    elif cmd == "all":
        sheet()
    # use search function
    elif cmd == "search":
        new_search()
    # add row to database
    elif cmd == "add":
        add_record()
    # delete row from database
    elif cmd == "delete":
        del_record()
    # exit the loop
    elif cmd == "exit":
        d = 1
    else:
        print("Invalid command.")
