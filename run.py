"""
This module provides functionality for interacting with
Google Sheets using the gspread library.
"""
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Expense tracker')

# expenses = SHEET.worksheet('Expenses')
# datas=expenses.get_all_values()


class Expense:
    """
    Class contains all the expense feilds to get from the user.
    """
    total_expense = 0

    def __init__(self, amount, category, details="", date_time=None):
        self.amount = amount
        self.category = category
        self.details = details
        self.date_time = date_time

    def __str__(self):
        """"
        Get the total expense from the user
        using to print the data in string format
        """
        return (f"\033[96mUpdated Expense Details:\n\n\033[0m"
                f"Cost: \033[93m{self.amount} euros\n\033[0m"
                f"Category:\033[93m {self.category}\n\033[0m"
                f"Details:\033[93m {self.details}\n\033[0m"
                f"date_time:\033[93m {self.date_time}\n\033[0m")

    @classmethod
    def sum_of_expense(cls):
        """
        Get the total expense from the user
        """
        cls.total_expense = 0
        worksheet = SHEET.worksheet("Expenses")
        all_expense_data = worksheet.get_all_values()
        for row in all_expense_data[1:]:
            actual_expense = row[0]
            expense_amount = float(actual_expense)
            cls.total_expense += expense_amount
        return cls.total_expense


class Income:
    """
    Get income details form the user
    """
    total_income = 0

    def __init__(self, income_amount, source, date_time):
        self.income_amount = income_amount
        self.source = source
        self.date_time = date_time

    def __str__(self):
        """"
        Get the total income from the user
        using to print the data in string format
        """
        return (f"\033[96mUpdated Income Details:\n\n\033[0m"
                f"Source:\033[93m{self.source}\n\033[0m"
                f"Income:\033[93m{self.income_amount} euros\n\033[0m"
                f"Date_time:\033[93m{self.date_time}\n\033[0m")

    @classmethod
    def sum_of_income(cls):
        """"
        Get the total income from the user
        """""
        cls.total_income = 0
        worksheet = SHEET.worksheet("Income")
        all_income_data = worksheet.get_all_values()
        for row in all_income_data[1:]:
            actual_income = row[1]
            income_amount = float(actual_income)
            cls.total_income += income_amount
        return cls.total_income


def get_expense_of_user():
    """
    Get the expenses form the user
    amount:int, category:string, details:string,date/time:date
    """
    print("=================")
    print("\033[96m Expense Details \033[0m")
    print("=================")
    print()
    text = "Enter the amount you spent (euros):\n"
    digit = 8
    cost = validate_user_income_or_expense(text, digit)
    user_selected_category = get_category()
    message = validate_expense_message()
    date_and_time = datetime.now().strftime("%d-%m-%y  %H:%M")
    user_expense_data = Expense(cost,
                                user_selected_category,
                                message,
                                date_and_time)
    return user_expense_data


def get_category():
    """
    Get the category of expense from the user
    """
    categories = ["Food", "Home", "Fun", "Car", "Misc"]

    while True:
        try:
            print("\033[96mExpense Categories:\033[0m")
            for i, name_of_category in enumerate(categories, 1):
                print(f" {i}. {name_of_category}")
            category_name_index = int(
                input("\n\033[94mSelect a category from [1-5]:\n\033[0m"))
            if category_name_index in range(1,len(categories)+1):
                selected_category = categories[category_name_index-1]
                return selected_category
            else:
                print()
                print("\033[91mInvalid category.\033[0m")
                print("\033[91mPlease enter a valid"
                      f" category [1-{len(categories)}]\033[0m")
                print()
        except ValueError:
            print()
            print("\033[91mInvalid category.\033[0m")
            print("\033[91mPlease enter a valid"
                  f" category [1-{len(categories)}]\033[0m")
            print()


def get_income_of_user():
    """
    Get income of the user
    """
    print("=================")
    print("\033[96m Income Details \033[0m")
    print("=================")
    print()
    text = "Give your income_amount (in euros):\n"
    digit = 9
    income = validate_user_income_or_expense(text, digit)
    income_details = validate_income_source()
    current_date_time = datetime.now().strftime("%d-%m-%y  %H:%M")
    user_income_data = Income(source=income_details,
                              income_amount=income,
                              date_time=current_date_time)
    return user_income_data


def validate_user_income_or_expense(prompt, max_digits):
    """
    Validate user income amount and
    expense amount for zero and negative values
    returns:
        float
    """

    while True:
        try:
            amount = float(input(prompt))
            if amount == 0:  # if input is 0
                print("\033[91mPlease give a valid amount,"
                      " 0 is not allowed\033[0m")
            elif amount < 0:  # input cannot be minus
                print("\033[91mPlease give a valid amount,"
                      " Negative values are not allowed\033[0m")
            elif len(str(amount).replace('.', '')) > max_digits:
                print("\033[91mPlease give a valid amount\033[0m")
                print(f"\033[91mMaximum {max_digits}"
                      " digits are allowed\033[0m")
                print("\033[91mIf the amount is"
                      f" greater than {max_digits} digits\033[0m")
                print("\033[91mPlease split it into"
                      " (10000000) and enter separately\033[0m")
            else:
                break
        except ValueError:
            print("\033[91mInvalid input."
                  " Please enter a valid number\033[0m")
    return amount


def validate_text_inputs(text, max_len):
    """
    Validate user expense details and
    income details within 25 chracters
    """
    while True:
        user_input = input(text)
        if len(user_input) == 0:
            print()
            print("\033[91mDetails cannot be empty\033[0m")
            print("\033[91mPlease enter some details within"
                  f" {max_len} characters.\n\033[0m")
        elif len(user_input) > max_len:
            print()
            print("\033[91mText is too long\033[0m")
            print("\033[91mPlease enter the data within"
                  f" {max_len} characters.\033[0m")
        else:
            break
    return user_input


def validate_expense_message():
    """
    Validates the expense message.
    This function validates the expense message and returns a status string.
    Returns:
        str: A status string indicating whether the expense message is valid.
    """
    text = "Enter the expense details within 25 characters:\n"
    data = validate_text_inputs(text, 25)
    return data


def validate_income_source():
    """
    Validates the  income details.
    This function validates the expense message and returns a status string.
    Returns:
        str: A status string indicating whether the expense message is valid.
    """
    text = "Enter the income details within 25 characters:\n"
    data = validate_text_inputs(text, 25)
    return data


def save_data_to_worksheet(data, worksheet_name):
    """
    Recevies data from user
    and inserted into relevant worksheet
    """
    print()
    print("\033[93mUpdating datas in"
          f" {worksheet_name} worksheet........\n\033[0m")
    print()
    worksheet = SHEET.worksheet(worksheet_name)

    if worksheet_name == "Expenses":
        data_list = [data.amount, data.category, data.details, data.date_time]
    elif worksheet_name == "Income":
        data_list = [data.source, data.income_amount, data.date_time]
    else:
        print("\033[91mInvalid worksheet,"
              " Please enter a valid worksheet name\033[0m")
        return

    worksheet.append_row(data_list)
    print(f"\033[93m{worksheet_name} worksheet updated successfully\033[0m")
    print()
    print(data)


def show_datas(worksheetname):
    """
    Shows the datas in the worksheet
    """
    worksheet = SHEET.worksheet(worksheetname)
    all_datas = worksheet.get_all_values()

    if worksheetname == "Expenses":
        if len(all_datas) <= 1:
            print("\033[91mNo expense data available\033[0m")
        else:
            print()
            print("===================================")
            print("\033[96m     EXPENSE DATAS RECORD\033[0m")
            print("===================================")
            print()
            print(f"{'Itm_No':9} {'Amount':^10} {'Category':^12}"
                  f"{'Details':^20} {'Date/Time':^25}")
            print("-"*80)
            expense_item = 0
            for row in all_datas[1:]:
                # looping to get all the row values form google sheet
                print(f"{(expense_item+1):^9} {row[0]:^10}"
                      f"{row[1]:^12} {row[2]:<25} {row[3]:<25}")
                expense_item += 1
    elif worksheetname == "Income":
        if len(all_datas) <= 1:
            print("\033[91mNo Income data available\033[0m")
        else:
            print()
            print("=====================================")
            print("\033[96m     INCOME DATAS RECORD\033[0m")
            print("=====================================")
            print()
            print(f"{'Itm_No':9} {'Income Type':<25}"
                  f"{'Actual Income':<15} {'Date/Time':^30}")
            print("-"*80)
            income_item = 0
            for row in all_datas[1:]:
                print(f"{(income_item+1):^9} {row[0]:<25}"
                      f"{row[1]:^15} {row[2]:^30}")
                print()
                income_item += 1
    else:
        pass


def summarize_expenses():
    """
    Summarize expenses by category
    returns:
        None
    """
    worksheet = SHEET.worksheet("Expenses")
    all_expense_data = worksheet.get_all_values()
    if len(all_expense_data) <= 1:
        print("\033[91mNo expense data available\033[0m")
        return

    sum_of_category = {}
    for row in all_expense_data[1:]:
        category = row[1]
        amount = float(row[0])
        if category in sum_of_category:
            sum_of_category[category] += amount
        else:
            sum_of_category[category] = amount
    print("=================================")
    print("\033[96m  EXPENSE SUMMARY BY CATEGORY \033[0m")
    print("=================================")
    print()
    for category, total in sum_of_category.items():
        print(f"{category}: \033[93m{total}\033[0m euros")

    max_category = max(sum_of_category, key=sum_of_category.get)
    max_expense = sum_of_category[max_category]

    print()
    print("You spent the most in the category")
    print(f"\033[93m{max_category}\033[0m"
          f" with a total of \033[93m{max_expense}"
        " \033[0m euros.")
    # access through class method sum of income
    income = Income.sum_of_income()
    # access through class method sum of expense
    expense = Expense.sum_of_expense()
    balance_amount = income-expense
    if expense < balance_amount:
        print()
        print("You have balance of \033[93m"
             f" {balance_amount}\033[0m euros from your income")
        print()
    elif expense > balance_amount:
        print()
        print("You have deficit of \033[93m"
             f" -{balance_amount}\033[0m euros from your income")
        print()
    else:
        print()
        print("\033[93mYou have no balance from your income\033[0m")
        print()


def delete_a_row(worksheetname):
    """
    Deleting a user specified row
    from the income or expense data"
    """
    worksheet = SHEET.worksheet(worksheetname)
    all_datas = worksheet.get_all_values()

    if worksheetname == "Expenses":
         # Check if there are no data records except the header row
        if len(all_datas) <= 1:
            print("\033[91mNo expense data available\033[0m")
            return

        show_datas("Expenses")
        print()
        print("==============================================")
        print("Which Expense item do you want to delete")
        print()
        while True:
            try:
                item = int(input("Enter the item number:\n"))
                if item > 0 and item <= (len(all_datas)-1):
                    worksheet.delete_rows(item + 1)
                    print()
                    print("\033[93mDeleted item:\033[0m", item)
                    print()
                    break
                else:
                    print()
                    print("\033[91mInvalid item."
                          " Please enter a valid item number.\033[0m\n")
            except ValueError:
                print()
                print("\033[91mInvalid Item,"
                      " Please enter a valid item number\033[0m\n")

    elif worksheetname == "Income":
        # Check if there are no data records except the header row
        if len(all_datas) <= 1:
            print("\033[91mNo income data available\033[0m")
            return

        show_datas("Income")
        print("==============================================")
        print("Which Income item do you want to delete")
        print()
        while True:
            try:
                # Asking user to input a number
                # Converting the input string to an integer
                item = int(input("Enter the item number:\n"))
                if item > 0 and item <= (len(all_datas)-1):
                    worksheet.delete_rows(item + 1)
                    print("\033[93mDeleted item:\033[0m\n", item)
                    break
                else:
                    print()
                    print("\033[91mInvalid item."
                          "Please enter a valid item number.\033[0m\n")
            except ValueError:
                print()
                print("\033[91mInvaid Item,"
                      "Please enter a valid item number\033[0m\n")
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
            print("\033[96m         WELCOME TO EXPENSIFY           \033[0m")
            print("========================================")
            print()
            print("HI, WHAT WOULD YOU LIKE TO DO TODAY?\n")
            print("Select an option from the following:")
            print()
            print("1.Manage Income")
            print("2.Manage Expenses")
            print("3.Help")
            print("4.Exit")
            print()
            user_input = int(input("\033[94mEnter you choice[1-4]:\n\033[0m"))
            print()
            if user_input == 1:
                income_menu_option()
            elif user_input == 2:
                expense_menu_options()
            elif user_input == 3:
                help_menu()
            elif user_input == 4:
                print("\033[92mEXITING FROM EXPENSIFY."
                      " HAVE A GOOD DAY\033[0m")
                print()
                break
            else:
                print("\033[91mInvalid Option ,"
                      "Please enter a valid option from [1-4]\033\033[0m")
        except ValueError:
            print()
            print("\033[91mInvalid Input ,"
                  "Please enter a number from (1-4)\033[0m")
            print()
        except KeyboardInterrupt:
            print("\033[91m\nKeyboard interruption"
                  " detected. Exiting...\033[0m")
            break


def income_menu_option():
    """
    Giving user the option for
    income field to add datas, show datas
    """
    income_options = ["Record new Income",
                      "View all Income",
                      "Delete Income data",
                      "Return to Main Menu"]
    while True:
        print("===========================")
        print("\033[96m    MANAGE INCOME MENU       \033[0m")
        print("===========================")
        print()

        for opt, options in enumerate(income_options, 1):
            print(f"{opt}.{options}")
        try:
            value_range = f"[1-{len(income_options)}]"
            print()
            selected_index = int(input("\033[94mSelect an option from"
                                       f"{value_range}:\n\033[0m"))
            print()

            if selected_index in range(len(income_options)+1):
                if selected_index == 1:
                    user_income_details = get_income_of_user()
                    save_data_to_worksheet(user_income_details, "Income")
                elif selected_index == 2:
                    show_datas("Income")
                elif selected_index == 3:
                    delete_a_row("Income")
                elif selected_index == 4:
                    print("\033[92mReturning to main menu...........\033[0m")
                    print()
                    break
                else:
                    print()
                    print("\033[91mInvalid option\033[0m")
                    print("\033[91mPlease enter a"
                          f" valid option from {value_range}\033[0m")
                    print()
            else:
                print()
                print("\033[91mInvalid option\033[0m")
                print("\033[91mPlease enter a valid"
                      f" option from {value_range}\033[0m")
                print()

        except KeyboardInterrupt:
            print()
            print("\n\033[91mKeyboard interruption detected."
                  "Returning to Main Menu...\033[0m")
            print()
            break
        except ValueError:
            print()
            print("\033[91mInvalid Input ,"
                  f"Please enter a number from {value_range}\033[0m")
            print()
            print()


def expense_menu_options():

    """
    Giving options for expense field to add datas,
    show datas and summerize expense
    """
    options = ["Record new Expense",
               "View all Expense",
               "Delete Expense",
               "Sumarize Expenses",
               "Return to Main Menu"]
    while True:
        print("===========================")
        print("\033[96m   MANAGE EXPENSES MENU    \033[0m")
        print("===========================")
        print()
        # looping to number the options
        for opt, option in enumerate(options, 1):
            print(f"{opt}.{option}")
        try:
            value_range = f"[1-{len(options)}]"
            print()
            user_choice = int(input("\033[94mSelect an option"
                                    f" from {value_range}:\n\033[0m"))
            if user_choice in range(len(options)+1):
                if user_choice == 1:
                    user_expense_details = get_expense_of_user()
                    save_data_to_worksheet(user_expense_details, "Expenses")
                elif user_choice == 2:
                    show_datas("Expenses")
                elif user_choice == 3:
                    delete_a_row("Expenses")
                elif user_choice == 4:
                    summarize_expenses()
                elif user_choice == 5:
                    print("\033[92mReturning to main menu.....\033[0m")
                    print()
                    break
                else:
                    print()
                    print("\033[91mInvalid option,\033[0m")
                    print("\033[91mPlease enter a"
                          f" valid option from {value_range}\033[0m")
                    print("---------------------------")
                    print()
            else:
                print()
                print("\033[91mInvalid option,\033[0m")
                print("\033[91mPlease enter a"
                      f" valid option from {value_range}\033[0m")
                print("----------------------------")
                print()
        except KeyboardInterrupt:
            print()
            print("\n\033[91mKeyboard interruption detected."
                  " Returning to Main Menu...\033[0m")
            print()
            break
        except ValueError:
            print()
            print("\033[91mInvalid Input ,"
                  f"Please enter a number from {value_range}\033[0m")
            print()


def help_menu():
    """
    Printing the help menu
    """
    print("\033[96mEXPENSIFY:Your Personal Expense Tracker\033[0m")
    print("-------------------------------------------"
          "------------------------------------")
    print("Expensify is a handy tool designed to\n\n"
          "help you manage your expenses efficiently.\n\n"
          "With Expensify, you can easily track your spending,\n\n"
          "record your income, and categorize your transactions \n\n"
          "to gain insights into your financial habits. \n\n")
    print("\033[96mManage Expenses Menu:\033[0m")
    print("-------------------------------------------"
          "----------------------------------")
    print("1.Record Expense:\n"
          "  Enter your expenses with"
          " amount spent, category, and details.\n")
    print("2.View Expenses:\n"
          "  See a summary of all recorded"
          " expenses with categories and dates.\n")
    print("3.Summarize Expense:\n"
          "  Get a breakdown of your"
          " expenses by category.\n")
    print("4.Delete Expense:\n"
          "  Delete an expense from the list.\n")
    print()
    print("\033[96mManage Income Menu:\033[0m")
    print("-------------------------------------------"
          "-----------------------------------")
    print("1.Record Income:\n"
          "  Enter your income with the amount"
          " received, source, and details.\n")
    print("2.View Income:\n"
          "  See a summary of all recorded income,"
          " including sources and dates.\n")
    print("3.Delete Income:\n"
          "  Delete an income from the list.\n")
    print()
    print("\033[96mInstructions:\033[0m")
    print("--------------------------------------------"
          "----------------------------------")
    print("1.All the cost must be in number values(Max 8 digits).\n")
    print("2.The details of income or expense"
          " within 25 characters.\n")
    print("3.Select options (Exit) accordingly to exit from the app")
    print()


def title():
    """
    Printing the title of the program
    """
    print("==================================="
          "==================================")
    print(r"***** *    * * ***\  ***** * *      * "
          "/****  ***** ***** *       * ")
    print(r"*      *  *  *     * *     *   *    * "
          "*        *   *       *    *  ")
    print(r"***     *    * ____* ***   *     *  * "
          "*****    *   *****     *     ")
    print(r"*      *  *  *       *     *        * "
          "     *   *   *         *     ")
    print(r"***** *    * *       ***** *        * "
          "*****  ***** *         *     ")
    print("======================================"
          "===============================")


def main():
    """
    Calling the functions
    """
    income_or_expense()


main()
