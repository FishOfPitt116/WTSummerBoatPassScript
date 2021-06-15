import spreadsheet as s
import sys

while True:
    currName = input("Type a name for account lookup. Type 0 to exit the program.") # Ask user for name
    if currName == '0':
        sys.exit(0)
    s.print_account_information(s.get_account_index(currName))