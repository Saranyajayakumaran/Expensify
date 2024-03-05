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
    """
    Class contains all the expense feilds to get from the user.
    """
    def __init__(self,amount,category,details="",date_time=None):
        self.amount=amount
        self.category=category
        self.details=details
        self.date_time=date_time

    def __str__(self):
        return f"Expense details:\nCost: {self.amount}euros,\nCategory: {self.category},\nDetails: {self.details},\ndate_time: {self.date_time}"
        
class Income:
    """
    Get income details form the user
    """
    def __init__(self,source,income_amount,date_time):
        self.source=source
        self.income_amount=income_amount
        self.date_time=date_time
    
    def __str__(self):
        return f"Income deatils:\nSource:{self.source},\nIncome:{self.income_amount},\nDate_Time:{self.date_time}"


def get_expense_of_user():
    """
    Get the expenses form the user
    amount:int, category:string, details:string,date/time:date
    """
    print("Enter the amount which you spent:")
    cost = validate_user_income_or_expense()
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

   
def get_income_of_user():
    """
    Get income of the user
    """
    print("============")
    print("Income Details")
    print("============")
    income_details=input("Give the source of income details:")
    print(f"you entered: {income_details}")
    print("Give your income_amount:")
    income= validate_user_income_or_expense()
    print(f"you entered: {income}")
    current_date_time=datetime.now().strftime("%d-%m-%y  %H:%M")
    print(f"{current_date_time}")

    user_income_data=Income(source=income_details,income_amount=income,date_time=current_date_time)
    return user_income_data


def validate_user_income_or_expense():
    while True:
        try:
            amount=float(input(""))
            if amount==0:
                print("Please give a valid amount, 0 is not allowed ")
            elif amount<0:
                print("Please give a valid amount, Negative values are not allowed")
            else:
                break
        except ValueError:
            print("Invalid input. please enter a valid number")
    return amount


def save_data_to_worksheet(data,worksheet_name):
    """
    Recevies data from user and inserted into relevant worksheet
    """
    print(f"updating datas in {worksheet_name} worksheet........\n")
    print()
    worksheet=SHEET.worksheet(worksheet_name)

    if worksheet_name=="Expenses":
        data_list=[data.amount,data.category,data.details,data.date_time]
    elif worksheet_name=="Income":
        data_list=[data.source,data.income_amount,data.date_time]
    else:
        print("Invalid data type")
        return

    worksheet.append_row(data_list)
    print(f"{worksheet_name}'worksheet updated successfully")
    print(data)


def show_expense_data():
    """
    Show all the expenses to the user in table
    """
    worksheet=SHEET.worksheet("Expenses")
    all_expense_data=worksheet.get_all_values()
    if len(all_expense_data)==0:
        print("No expense data available")
    else:
        print(f"Expense datas:")
        print("{:<15} {:<15} {:<35} {:<20}".format("Amount(euro)","Category","Details","Date/Time"))
        print("-"*100)
        for row in all_expense_data[1:]:
            print("{:<15} {:<15} {:<35} {:<20}".format(*row))
            
def show_income_data():
    """
    Show all the Incomes to the user in table
    """
    worksheet=SHEET.worksheet("Income")
    all_income_data=worksheet.get_all_values()
    if len(all_income_data)==0:
        print("No Income data available")
    else:
        print(f"Income datas:")
        print("{:<25} {:<15} {:<15}".format("Income Type","Actual Income","Date/Time"))
        print("-"*65)
        for row in all_income_data[1:]:
            print("{:<25} {:<15} {:<15}".format(*row))
                

    
#user_expense_details=get_expense_of_user()
        
#save_data_to_worksheet(user_expense_details,"Expenses")
def summerize_expenses():
    print("Expense summerize")

def delete_expense():
    print("expense deleted")

def income_or_expense():
    """
    ask user which field they want to choose income or expense
    """
    while True:
        try:
            print("========================================")
            print("         WELCOME TO EXPENSIFY         ")
            print("========================================")
            print()
            print("What would you like to do today?")
            print("Select an option from the following:")
            print()
            print("1.Manage Income(I/i)")
            print("2.Manage Expense(E/e)")
            print("3.Exit(X/x)")
            print()
            user_input=int(input("Enter your Choice[1-3]:"))
            print()
            if user_input==1:
                income_menu_option()    
            elif user_input==2:
                expense_menu_options()
            elif user_input==3:
                print("Exiting the program. Goodbye!")
                break     
            else:
                print("invalid input, please select (1-3)")
        
        except KeyboardInterrupt:
            print("\nKeyboard interruption detected. Exiting...")
            break
        
        except Exception as e:
            print()
            print("invalid input, please select (1-3)")
            print()



def income_menu_option():
    """
    Giving user the option for income field to add datas, show datas
    """
    income_options=["Record new income","View all income","Return to Main Menu"]

    while True:
        print()
        print("****Options****")
        for opt,options in enumerate(income_options,1):
            print(f"{opt}.{options}")
        try:
            value_range=f"[1-{len(income_options)}]"
            print()
            selected_index=int(input(f"Select an option {value_range}"))
            print()
            print(f"you have selected: {selected_index}")
            
            
            if selected_index in range(len(income_options)+1):
                if selected_index== 1:
                    user_income_details=get_income_of_user()
                    save_data_to_worksheet(user_income_details,"Income")  
                elif selected_index== 2:
                   show_income_data()
                elif selected_index==3:
                    print("Returning to main menu...........")
                    break
                else:
                    print()
                    print("Invalid option, try again")
                    print("---------------------------")
            else:
                print()
                print("Invalid option, try again")
                print("---------------------------")

        except KeyboardInterrupt:
            print("\nKeyboard interruption detected. Exiting...")
            break
            
        except:
            print()
            print(f"Invalid Input ,Please enter a number from {value_range}")
            print()
            print()




def expense_menu_options():

    """
    Giving options for expense field to add datas, show datas and summerize expense
    """
    options=["Record new Expense","View all expense","Summerize Expenses","Delete Expense","Return to Main Menu"]

    while True:
        print("****Options****")
        print()
        for opt, option in enumerate(options,1):
           print(f"{opt}.{option}")
        try:
            value_range=f"[1-{len(options)}]"
            print()
            user_choice=int(input(f"Select an option {value_range}:"))
            print()
            print(f"you ave selected:  {user_choice}")
            print()

    
            if user_choice in range(len(options)+1):
                if user_choice== 1:
                    user_expense_details=get_expense_of_user()
                    save_data_to_worksheet(user_expense_details,"Expenses")
                elif user_choice== 2:
                   show_expense_data()
                elif user_choice== 3:
                    summerize_expenses()
                elif user_choice== 4:
                    delete_expense()
                elif user_choice== 5:
                    print("Returning to main menu.....")
                    break
                else:
                    print()
                    print(f"Invalid option, try again please enter a numnber from{value_range}")
                    print("---------------------------")
                    print()
            else:
                print()
                print(f"Invalid option, try again please enter a numnber from{value_range}")
                print("----------------------------")
                print()
        
        except KeyboardInterrupt:
            print("\nKeyboard interruption detected. Exiting...")
            break
        
        except ValueError:
            print()
            print(f"Invalid Input ,Please enter a number from {value_range}")
            print()

def main():
    income_or_expense()


main()
