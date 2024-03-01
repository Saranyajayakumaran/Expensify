import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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

class Expense:
    def __init__(self,amount,category,details="",date_time=None):
        self.amount=amount
        self.category=category
        self.details=details
        self.date_time=date_time

    def __str__(self):
        return f"Expense details:\nCost: {self.amount}euros,\nCategory: {self.category},\nDetails: {self.details},\ndate_time: {self.date_time}"
        


expense_list=[]  

def get_expense_of_user():
    """
    Get the expenses form the user
    amount:int, category:string, details:string,date/time:date
    """

    cost = float(input("Enter the amount which you spent:"))
    print(f"you have entered : {cost} euros")
    user_selected_category=get_category()
    print(user_selected_category)
    message=input("Enter the detail of the expense:")
    print(f"you entered {message}")
    date_and_time=datetime.now().strftime("%d-%m-%y  %H:%M")
    print(date_and_time)

    user_expense_data=Expense(amount=cost,category=user_selected_category,details=message,date_time=date_and_time)
    return user_expense_data

    
def get_category():
    """
    Get the category of expense from the user 
    """
    categories=["Food","Home","Fun","Car","Miscellenious"]

    while True: 
        try:
            for i , name_of_category in enumerate(categories,1):
                print(f" {i}. {name_of_category}")
            category_name_index=int(input("Select a category:"))-1
            print(f"you selected:{category_name_index}")
            
            if category_name_index in range(len(categories)):
                selected_category=categories[category_name_index]
                return selected_category
                
            else:
                print(f"Invalid category . Please enter a valid ocategory from {[1-{len(categories)}]}")
        except Exception as e:
            print(f"Invalid category . Please enter a valid ocategory from {[1-{len(categories)}]}")



def save_expense_to_file(data):
    """
    Update the user expense details in the google sheet
    add the values in new row
    """
    print()
    print("updating datas in worksheet........\n")
    expense_worksheet=SHEET.worksheet("Expenses")
    expense_data=[data.amount,data.category,data.details,data.date_time]
    expense_worksheet.append_row(expense_data)
    print("Expense worksheet updated successfully........\n")
    print(f"{data}")


#user_expense_details=get_expense_of_user()
#save_expense_to_file(user_expense_details)



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
                print("invalid input, please select I or E or X")
        except Exception as e:
            print()
            print("invalid input, please select I or E or X")
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
                    user_expense_details=get_expense_of_user()
                    save_expense_to_file(user_expense_details)
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
