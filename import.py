from sys import argv, exit
import csv
from cs50 import SQL

# Create/rewrite db file
open("students.db", "w").close()

# Open file for SQLite
db = SQL("sqlite:///students.db")

# Create a table on database
db.execute("CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, first VARCHAR(255), middle VARCHAR(255), last VARCHAR(255), house VARCHAR(10), birth INTEGER)")

# If arguments not correct show usage
if len(argv) != 2:
    print("Usage: python import.csv file.csv")
    exit(1)

# Open csv and read contents into memory
else:
    with open(f"{argv[1]}", "r", newline='') as characters:

        # Create dictionary reader
        reader = csv.DictReader(characters)

        for row in reader:

            # Split each name into first, middle and last names list
            split_names = row["name"].split(' ')

            if len(split_names) == 2:

                # Record each item into database
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                           split_names[0], 'NULL', split_names[1], row["house"], row["birth"])

            if len(split_names) == 3:

                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                           split_names[0], split_names[1], split_names[2], row["house"], row["birth"])