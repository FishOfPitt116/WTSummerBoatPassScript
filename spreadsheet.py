import sys, gspread
import searchandsort as sas

gc = gspread.service_account() # Authentication works on my laptop only

sh = gc.open("Test Boat Passes").sheet1 # Calls the spreadsheet named "Test Boat Passes" in drive


# print(sh.col_values(1))

# print(sh.get_all_values())

names = sh.col_values(1) # List of all names in our system
# print(names)
while True:
    currName = input("Type a name for account lookup. Type 0 to exit the program.") # Ask user for name
    if currName == '0':
        sys.exit(0)
    index = sas.search(names, currName) + 1
    try:
        print(sh.row_values(index))
    except:
        print('Account not found.')