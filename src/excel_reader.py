from openpyxl import load_workbook
from datetime import date

class ExcelReader:
    def __init__(self, file_path: str, column_no: int) -> None:
        self.celebrants: list = []
        self.column_no: int = column_no
        self.workbook = load_workbook(file_path)

    def set_active_sheet(self, sheet_name: str):
        self.active_sheet = self.workbook[sheet_name]

    def get_celebrants_from_file(self):
        today_day = date.today().day
        today_month = date.today().month
        self.max_row = self.active_sheet.max_row
        for row_num in range(2, self.max_row+1):
            birthday = self.active_sheet.cell(row=row_num, column=self.column_no)
        
            if birthday.value.day == today_day and birthday.value.month == today_month:
                first_name = self.active_sheet.cell(row=row_num, column=1).value
                last_name = self.active_sheet.cell(row=row_num, column=2).value
                full_name = first_name + " " + last_name
                self.celebrants.append(full_name)

        return self.celebrants
