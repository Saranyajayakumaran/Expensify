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
    print(f"you have entered : {cost} euros")

    categories=["Food","Rent","Fun","Car","Miscellenious"]

    while True: 
        for i , name_of_category in enumerate(categories,1):
            print(f" {i}. {name_of_category}")
        category_name=input("Select a category:",i)
        print(f"you selcted:{category_name}")
        break
    
def  show_all_expense():
    print("All the expenses")
    
def summerize_expenses():
    print("Expense summerize")

def delete_expense():
    print("expense deleted")

def get_user_income():
    print("get the income")

def income_or_expense():
    while True:
        try:
            print("-----------------------")
            print("Welcome to Expensify")
            print("-----------------------")
            print()
            print("SELECT AN OPTION")
            user_input=input("Income(i/I) or Expense(e/E) or Exit (x):")
            print()
            if user_input=='I' or user_input =='i':
                get_user_income()
            elif user_input=='E'or user_input =='e':
                menu_options()
            elif user_input=='X' or user_input=='x':
                print("Exiting the program. Goodbye!")
                break     
            else:
                print("invalid input, please select I or E")
        except Exception as e:
            print()
            print("invalid input, please select I or E")
            print()

def menu_options():
    options=["Add the expense","Show all the expense","Summerize expense","Delete expense","Exit"]

    while True:
        print("****Options****")
        print()
        for opt, option in enumerate(options,1):
           print(f"{opt}.{option}")
        try:
            value_range=f"[1-{len(options)}]"
            user_choice=int(input(f"Select an option {value_range}:"))
            print(f"you ave selected:  {user_choice}")

    
            if user_choice in range(len(options)+1):
                if user_choice== 1:
                    get_expense_of_user()
                elif user_choice== 2:
                    show_all_expense()
                elif user_choice== 3:
                    summerize_expenses()
                elif user_choice== 4:
                    delete_expense()
                elif user_choice== 5:
                    print("Exting.....")
                    break

                else:
                    print()
                    print("Invalid option, try again")
                    print("---------------------------")
                    print()
            else:
                print()
                print("Invalid option, try again")
                print("----------------------------")
                print()
        except:
            print()
            print(f"Invalid Input ,Please enter a number from {value_range}")
            print()

def main():
    income_or_expense()


main()