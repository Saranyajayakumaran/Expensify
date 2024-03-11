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
    total_expense=0
    def __init__(self,amount,category,details="",date_time=None):
        self.amount=amount
        self.category=category
        self.details=details
        self.date_time=date_time

    def __str__(self):
        return f"Updated Expense Details:\n\nCost: {self.amount}euros,\nCategory: {self.category},\nDetails: {self.details},\ndate_time: {self.date_time}"
    
    @classmethod
    def sum_of_expense(cls):
        cls.total_expense=0
        worksheet = SHEET.worksheet("Expenses")
        all_expense_data = worksheet.get_all_values()
        for row in all_expense_data[1:]:
            actual_expense=row[0]
            expense_amount=float(actual_expense)
            cls.total_expense+=expense_amount
        return cls.total_expense


            
class Income:
    """
    Get income details form the user
    """
    total_income=0
    def __init__(self,income_amount,source,date_time):
        self.income_amount=income_amount
        self.source=source
        self.date_time=date_time
    
    def __str__(self):
        return f"Updated Income Details:\n\n,Source:{self.source},\nIncome:{self.income_amount},\nDate_Time:{self.date_time}"
    
    @classmethod
    def sum_of_income(cls):
        cls.total_income=0
        worksheet = SHEET.worksheet("Income")
        all_income_data = worksheet.get_all_values()
        for row in all_income_data[1:]:
            actual_income=row[1]
            income_amount=float(actual_income)
            cls.total_income+=income_amount
        return cls.total_income


def get_expense_of_user():
    """
    Get the expenses form the user
    amount:int, category:string, details:string,date/time:date
    """
    print("=================")
    print(" Expense Details ")
    print("=================")
    print("Enter the amount which you spent:")
    cost = validate_user_income_or_expense()
    #print(f"you have entered : {cost} euros")
    user_selected_category=get_category()
    #print(user_selected_category)
    message=validate_expense_message()
    #print(f"you entered {message}")
    date_and_time=datetime.now().strftime("%d-%m-%y  %H:%M")
    #print(date_and_time)

    user_expense_data=Expense(amount=cost,category=user_selected_category,details=message,date_time=date_and_time)
    #print("You have entered:",user_expense_data)
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
            category_name_index=int(input("Select a category from [1-5]:\n"))-1
            #print(f"you selected:{category_name_index+1}")
            
            if category_name_index in range(len(categories)):
                selected_category=categories[category_name_index]
                return selected_category
                
            else:
                print(f"Invalid category . Please enter a valid category from {[1-{len(categories)}]}")
        except Exception as e:
            print(f"Invalid category . Please enter a valid category from {[1-{len(categories)}]}")

   
def get_income_of_user():
    """
    Get income of the user
    """
    print("=================")
    print("  Income Details ")
    print("=================")
    print("Give your income_amount:")
    income= validate_user_income_or_expense()
    #print(f"you entered: {income}")
    income_details=validate_income_source()
    #print(f"you entered: {income_details}")
    current_date_time=datetime.now().strftime("%d-%m-%y  %H:%M")
    #print(f"{current_date_time}")

    user_income_data=Income(source=income_details,income_amount=income,date_time=current_date_time)
    return user_income_data

def validate_user_income_or_expense():
    """
    Validate user income amount and expense amount for zero and negative values
    """
    while True:
        try:
            amount=float(input("\n"))
            if amount==0:#if input is 0
                print("Please give a valid amount, 0 is not allowed ")
            elif amount<0:
                print("Please give a valid amount, Negative values are not allowed")
            else:
                break
        except ValueError:
            print("Invalid input. please enter a valid number")
    return amount


def validate_text_inputs(text,max_len):
    """
    Validate user expense details and income details within 25 chracters
    """
    while True:
            user_input=input(text)
            if len(user_input)>max_len:
                print(f"Please enter the data within {max_len} characters.")
            else:
                break
    return user_input

def validate_expense_message():
    data=validate_text_inputs("Enter the expense details within 25 characters:\n",25)
    return data

def validate_income_source():
    data=validate_text_inputs("Enter the income details within 25 characters:\n",25)
    return data
   

def save_data_to_worksheet(data,worksheet_name):
    """
    Recevies data from user and inserted into relevant worksheet
    """
    print(f"Updating datas in {worksheet_name} worksheet........\n")
    print()
    worksheet=SHEET.worksheet(worksheet_name)

    if worksheet_name=="Expenses":
        data_list=[data.amount,data.category,data.details,data.date_time]
    elif worksheet_name=="Income":
        data_list=[data.source,data.income_amount,data.date_time]
    else:
        print("Invalid data")
        return

    worksheet.append_row(data_list)
    print()
    print(f"{worksheet_name}'worksheet updated successfully")
    print()
    print(data)
   


def show_datas(worksheetname):
    worksheet=SHEET.worksheet(worksheetname)
    all_datas=worksheet.get_all_values()

    if worksheetname=="Expenses":
        if len(all_datas)==0:
            print("No expense data available")
        else:
            print(f"EXPENSE DATAS RECORD")
            print()
            print("{:15} {:<15} {:<15} {:<25} {:<20}".format("ItemNumber","Amount(euro)","Category","Details","Date/Time"))
            print("-"*100)
            expense_item = 0
            for row in all_datas[1:]: # looping to get all the row values form google sheet
                print("{:^15}  {:<15} {:<15} {:<25} {:<20}".format(expense_item+1, *row))
                expense_item += 1
    elif worksheetname=="Income":
        if len(all_datas)==0:
            print("No Income data available")
        else:
            print(f"INCOME DATAS RECORD")
            print()
            print("{:15} {:<20} {:<15} {:<15}".format("ItemNumber","Income Type","Actual Income","Date/Time"))
            print("-"*65)
            income_item = 0
            for row in all_datas[1:]:
                print("{:^15} {:<20} {:<15} {:<15}".format(income_item+1,*row))  
                income_item += 1
    else:
        pass
            
            

def summarize_expenses():
    """
    Summarize expenses by category
    """
    worksheet = SHEET.worksheet("Expenses")
    all_expense_data = worksheet.get_all_values()
    if len(all_expense_data) == 0:
        print("No expense datas available")
    else:
        sum_of_category = {}
        for row in all_expense_data[1:]: 
            category = row[1]
            amount = float(row[0])
            if category in sum_of_category:
                sum_of_category[category] += amount
            else:
                sum_of_category[category] = amount
        print("=============================")
        print(" EXPENSE SUMMARY BY CATEGORY ")
        print("=============================")
        print()
        for category, total in sum_of_category.items():
            print(f"{category}: {total} euros")

        max_category = max(sum_of_category, key=sum_of_category.get)
        max_expense = sum_of_category[max_category]

        print()
        print(f"You spent the most in the category '{max_category}' with a total of {max_expense} euros.")

        income=Income.sum_of_income()
        expense=Expense.sum_of_expense()

        balance_amount=income-expense
        print()
        print(f"You have balance of {balance_amount} from your income")
        print()

def delete_a_row(worksheetname):
        
    worksheet= SHEET.worksheet(worksheetname)
    all_datas=worksheet.get_all_values()

    if worksheetname=="Expenses":
        show_datas("Expenses")
        print()
        print("==============================================")
        print("Which Expense item you want to delete")
        print()
        item = int(input("Enter the item number:\n"))


        if item > 0 and item <= len(all_datas):
            try:
                worksheet.delete_rows(item + 1)
                print("deleted item ! ",item)
            except gspread.exceptions.APIError as e:
                print(f"An error occurred: {e}")
            except AttributeError:
                print("Function is not available")
        else:
            print("Invalid item. Please enter valid item.")
    
    elif worksheetname=="Income":
        show_datas("Income")
        print("==============================================")
        print("Which Income item you want to delete")
        item = int(input("Enter the item number:\n"))

        if item > 0 and item <= len(all_datas):
            try:
                worksheet.delete_rows(item + 1)
                print("deleted item ! ",item)
            except gspread.exceptions.APIError as e:
                print(f"An error occurred: {e}")
            except AttributeError:
                print("Function is not available")
        else:
            print("Invalid item. Please enter valid item.")
    else:
        pass




def income_or_expense():
    """
    ask user which field they want to choose income or expense
    """
    title()
    while True:
        try:
            print("========================================")
            print("         WELCOME TO EXPENSIFY           ")
            print("========================================")
            print()
            print("What would you like to do today?")
            print("Select an option from the following:")
            print()
            print("1.Manage Income")
            print("2.Manage Expenses")
            print("3.Exit")
            print()
            user_input=int(input("Enter you choice[1-3]:\n"))
            print()
            if user_input==1:
                income_menu_option()    
            elif user_input==2:
                expense_menu_options()
            elif user_input==3:
                print("Exiting from the App. HAVE A GOOD DAY")
                print()
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
    income_options=["Record new income","View all income","Delete Income data","Return to Main Menu"]

    while True:
        print()
        print("===========================")
        print("   MANAGE INCOME MENU      ")
        print("===========================")
        print()

        for opt,options in enumerate(income_options,1):
            print(f"{opt}.{options}")
        try:
            value_range=f"[1-{len(income_options)}]"
            print()
            selected_index=int(input(f"Select an option from the following {value_range}:\n"))
            print()
            print(f"you have selected: {selected_index}")
            
            
            if selected_index in range(len(income_options)+1):
                if selected_index== 1:
                    user_income_details=get_income_of_user()
                    save_data_to_worksheet(user_income_details,"Income")  
                elif selected_index== 2:
                    show_datas("Income")
                elif selected_index== 3:
                    delete_a_row("Income")
                elif selected_index== 4:
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
            print()
            print("\nKeyboard interruption detected. Exiting...")
            print()
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
        print()  
        print("===========================")
        print("   MANAGE EXPENSES MENU    ")
        print("===========================")
        print()
        for opt, option in enumerate(options,1): #looping to number the options
           print(f"{opt}.{option}")
        try:
            value_range=f"[1-{len(options)}]"
            print()
            user_choice=int(input(f"Select an option from the following {value_range}:\n"))
            print()
            print(f"you ave selected:  {user_choice}")
            print()

    
            if user_choice in range(len(options)+1):
                if user_choice== 1:
                    user_expense_details=get_expense_of_user()
                    save_data_to_worksheet(user_expense_details,"Expenses")
                elif user_choice== 2:
                   show_datas("Expenses")
                elif user_choice== 3:
                    summarize_expenses()
                elif user_choice== 4:
                    delete_a_row("Expenses")
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
            print()
            print("\nKeyboard interruption detected. Exiting...")
            print()
            break
        
        except ValueError:
            print()
            print(f"Invalid Input ,Please enter a number from {value_range}")
            print()

def title():
    print(r"  _____   _     _   _____     _____   __    __   ______    ________   ______  _ _  __  ")
    print(r" |  ____|\ \   / / |   _ \  |  ____| |  \  |  | |   __  \ |__    __| |  ____| \  \/  / ")
    print(r" | |___   \ \ / /  |  |_| \ | |____  |   \ |  | \  \  \_|    |  |    |  |___   \    /  ")
    print(r" |  ___|   \ \ /   |  _ __| |  ____| |    \   |  __  \__     |  |    |  ____|   \  /   ")
    print(r" | |____   / / \   |  |     | |____  |  |\    | |  |_   |  __|  |__  |  |     _ / /    ")
    print(r" |______| / /   \  |__|     |______| |__| \__ | \___  _ / |________| |__|    |___/     ")
    print(r"                                                                                       ")

def main():
    income_or_expense()


main()
