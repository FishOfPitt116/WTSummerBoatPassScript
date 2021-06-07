import gspread
import searchandsort as sas

gc = gspread.service_account()

sh = gc.open("Test Boat Passes").sheet1


# print(sh.col_values(1))

# print(sh.get_all_values())

names = sh.col_values(1)
print(names)
currName = input("Type the name of the account you are trying to look up: ")

index = sas.search(names, currName) + 1
print(sh.row_values(index))