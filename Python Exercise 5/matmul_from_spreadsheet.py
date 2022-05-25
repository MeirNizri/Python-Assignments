import gspread
import numpy as np

def matmul_from_spreadsheet():
    # open spreadsheet
    account = gspread.service_account("credentials.json")
    spreadsheet = account.open("Matrix Multiplication")

    # create sheets
    sheet1 = spreadsheet.worksheet("A")
    sheet2 = spreadsheet.worksheet("B")
    sheet3 = spreadsheet.worksheet("A_times_B")

    # read
    m1 = sheet1.get_all_values()
    m2 = sheet2.get_all_values()
    m1 = [list(map(int, num)) for num in m1]
    m2 = [list(map(int, num)) for num in m2]

    # calculate multiplication and update sheet
    result = np.matmul(m1, m2)
    sheet3.clear()
    for i, row in enumerate(result):
        for j, num in enumerate(row):
            sheet3.update_cell(i+1, j+1, str(num))

if __name__ == '__main__':
    matmul_from_spreadsheet()
