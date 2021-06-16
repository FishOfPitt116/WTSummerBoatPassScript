import sys, gspread
import searchandsort as sas

gc = gspread.service_account() # Authentication works on my laptop only
sh = gc.open("Test Boat Passes").sheet1 # Calls the spreadsheet named "Test Boat Passes" in drive
names = sh.col_values(1) # List of all names in our system

def sort_sheet_by_name():
    sh.sort((1, 'asc'))

def get_account_index(currName):
    return sas.search(names, currName) + 1

def print_account_information(accountIndex):
    try:
        print(sh.row_values(accountIndex))
    except:
        print('Account not found.')

def add_20_pass(accountIndex):
    currPasses = str(sh.cell(accountIndex, 2).value)
    if currPasses == "None":
        currPasses = ""
    currPasses += "X"
    sh.update_cell(accountIndex, 2, currPasses)

def add_50_pass(accountIndex):
    currPasses = str(sh.cell(accountIndex, 3).value)
    if currPasses == "None":
        currPasses = ""
    currPasses += "X"
    sh.update_cell(accountIndex, 3, currPasses)

def new_account(name):
    sh.update_cell(len(names)+1, 1, name)
    print('New account created under name', name)
    sort_sheet_by_name()