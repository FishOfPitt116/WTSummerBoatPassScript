import sys, gspread
import searchandsort as sas
from datetime import datetime

gc = gspread.service_account() # Authentication works on my laptop only
sh = gc.open("Test Boat Passes").sheet1 # Calls the spreadsheet named "Test Boat Passes" in drive
names = sh.col_values(1) # List of all names in our system

today = datetime.now().strftime("%m/%d/%Y")

def sort_sheet_by_name():
    sh.sort((1, 'asc'))

def get_account_index(currName):
    return sas.search(names, currName) + 1

def account_found(accountIndex):
    if accountIndex >= 2 and accountIndex <= len(names):
        return True
    else:
        return False

def print_account_information(accountIndex):
    if account_found(accountIndex):
        print()
        print('Account Name:', sh.cell(accountIndex, 1).value)
        print('Amount Remaining: $', sh.cell(accountIndex, 7).value)
        print('Date added:', sh.cell(accountIndex, 8).value)
        print()
    else:
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
    sh.update_cell(len(names)+1, 6, 0)
    sh.update_cell(len(names)+1, 8, today)
    print('New account created under name', name)

def make_purchase(val, accountIndex):
    currentAmount = int(sh.cell(accountIndex, 6).value)
    newAmount = currentAmount + val
    sh.update_cell(accountIndex, 6, newAmount)

def update_global_variables():
    gc = gspread.service_account()
    sh = gc.open("Test Boat Passes").sheet1
    names = sh.col_values(1)