import spreadsheet as s
import sys

while True:
    currName = input("Type a name for account lookup. \nType 0 to exit the program. \nType 1 to add an account.") # Ask user for name
    print()
    if currName == '0':
        sys.exit(0)
    elif currName == '1':
        newName = input("Please type the new account name.")
        print()
        actIndex = s.get_account_index(newName)
        if s.account_found(actIndex):
            print("Account already found. Printing information...")
        else:
            s.new_account(newName)
            continue
    actIndex = s.get_account_index(currName)
    s.print_account_information(s.get_account_index(currName))
    # s.print_account_information(s.get_account_index(currName))