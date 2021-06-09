from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")

# If arguments not correct show usage
if len(argv) != 2:
    print("Usage: python roaster.csv house")
    exit(1)

else:
    dict = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last",
                      argv[1])

    for row in dict:

        if row["middle"] != "NULL":
            print(row["first"], row["middle"], row["last"], ", born", row["birth"])

        else:
            print(row["first"], row["last"], ", born", row["birth"])