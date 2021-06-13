import gspread
import searchandsort as sas

gc = gspread.oauth() # Opens google account authentication

sh = gc.open("Test Boat Passes").sheet1 # Calls the spreadsheet named "Test Boat Passes" in drive


# print(sh.col_values(1))

# print(sh.get_all_values())

names = sh.col_values(1) # List of all names in our system
# print(names)
currName = input("Type the name of the account you are trying to look up: ") # Ask user for name

index = sas.search(names, currName) + 1
print(sh.row_values(index))
