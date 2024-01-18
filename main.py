import csv
import pandas as pd

def ssprint():
    pd.set_option('display.width', None)
    file_path = 'DBEC.csv'
    df = pd.read_csv(file_path)
    print(df)

def search_csv(file_path, search_term):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)

        headers = next(csv_reader, None)

        for row in csv_reader:
            if search_term in row:
                return row
    return None

def add_record():
    print("Type Course Number")
    course = input()[:5] # limits no. of characters to 5, etc.
    course = str(course) # makes sure input is always a string
    print("Type Course Name:")
    name = input()[:30]
    name = str(name)
    print("Type Number of Credits:")
    credits = input()[:1]
    credits = str(credits)
    print("Type Department Abbreviation:")
    dept = input()[:4]
    dept = str(dept)
    dept = dept.upper() # makes abbreviation all caps
    print("Type Description (max 100 char):")
    desc = input()[:100]
    desc = str(desc)
    print(course, name, credits, dept, desc)
    new_record = {course, name, credits, dept, desc}
    file_path = 'DBEC.csv'
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
    print("nothing")

# main loop
d = 0
while d == 0:
    print("Type Sheet, Search or Exit")
    cmd = input()
    cmd = cmd.lower()
    # pull whole spreadsheet function
    if cmd == "sheet":
        ssprint()
    # pull search function
    elif cmd == "search":
        r = 0
        while r == 0:
            print("Enter Search Term")
            file_path = 'DBEC.csv'
            search_term = input()
            if search_term == "exit":
                r = 1
            else:
                result = search_csv(file_path, search_term)
                if result:
                    print(f"Found: {result}")
                else:
                    print("Search term not found.")
    # exit the loop
    elif cmd == "add":
        add_record()
    elif cmd == "delete":
        del_record()
    elif cmd == "exit":
        d = 1
    else:
        print("error")