import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS=Credentials.from_service_account_file('creds.json')
SCOPED_CREDS=CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT=gspread.authorize(SCOPED_CREDS)
SHEET=GSPREAD_CLIENT.open('Expense tracker')

expenses = SHEET.worksheet('Expenses')
datas=expenses.get_all_values()
print(datas)

class Expense:
    def __init__(self,amount,category,details="",date_time=None):
        self.amount=amount
        self.category=category
        self.details=details
        self.date_time=date_time



def get_expense_of_user():
    """
    Get the expenses form the user
    amount:int, category:string, details:string,date/time:date
    """
    cost = float(input("Enter the amount which you spent:"))
    print(f"you have entered the {cost}")
    expense_name=input("Enter the Category of expense:")
    print(f"You have entered{expense_name}")
    


get_expense_of_user()