import sys, gspread
import searchandsort as sas

gc = gspread.service_account() # Authentication works on my laptop only
sh = gc.open("Test Boat Passes").sheet1 # Calls the spreadsheet named "Test Boat Passes" in drive
names = sh.col_values(1) # List of all names in our system

def get_account_index(currName):
    return sas.search(names, currName) + 1
    
def print_account_information(accountIndex):
    try:
        print(sh.row_values(accountIndex))
    except:
        print('Account not found.')