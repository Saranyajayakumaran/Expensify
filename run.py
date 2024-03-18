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

# ANSI clor values
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'

# Reset color
RESET = '\033[0m'


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
        return (f"{CYAN}Updated Expense Details:\n\n{RESET}"
                f"Cost     : {YELLOW}{self.amount} euros\n{RESET}"
                f"Category : {YELLOW}{self.category}\n{RESET}"
                f"Details  : {YELLOW}{self.details}\n{RESET}"
                f"date_time: {YELLOW}{self.date_time}\n{RESET}")

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
        return (f"{CYAN}Updated Income Details:\n\n{RESET}"
                f"Source   :{YELLOW}{self.source}\n{RESET}"
                f"Income   :{YELLOW}{self.income_amount} euros\n{RESET}"
                f"Date_time:{YELLOW}{self.date_time}\n{RESET}")

    @classmethod
    def sum_of_income(cls):
        """"
        Get the total income from the user
        returns the total income
        """
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
    print(CYAN + "Expense Details " + RESET)
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
            print(CYAN+"Expense Categories:" + RESET)
            for i, name_of_category in enumerate(categories, 1):
                print(f" {i}. {name_of_category}")
            prompt = f"\n{BLUE}Select a category from [1-5]:\n{RESET}"
            category_name_index = int(input(prompt))
            if category_name_index in range(1, len(categories)+1):
                selected_category = categories[category_name_index-1]
                return selected_category
            else:
                print()
                print(RED + "Invalid category." + RESET)
                print(RED + "Please enter a valid"
                      f" category [1-{len(categories)}]" + RESET)
                print()
        except ValueError:
            print()
            print(RED + " Category must be a number." + RESET)
            print(RED + "Please enter a valid"
                  f" category number [1-{len(categories)}]" + RESET)
            print()


def get_income_of_user():
    """
    Get income of the user
    """
    print("=================")
    print(CYAN + "Income Details " + RESET)
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
                print()
                print(RED + "Please give a valid amount,"
                      " 0 is not allowed" + RESET)
                print()
            elif amount < 0:  # input cannot be minus
                print()
                print(RED + "Please give a valid amount,"
                      " Negative values are not allowed" + RESET)
                print()
            elif len(str(amount).replace('.', '')) > max_digits:
                print()
                print(RED + "Please give a valid amount" + RESET)
                print(RED + f"Maximum {max_digits}"
                      " digits are allowed" + RESET)
                print(RED + "If the amount is"
                      f" greater than {max_digits} digits" + RESET)
                print(RED + "Please split it into"
                      " (10000000) and enter separately" + RESET)
                print()
            else:
                break
        except ValueError:
            print(RED + "Invalid input."
                  " Please enter a valid number" + RESET)
            print()
    return amount


def validate_text_inputs(text, max_len):
    """
    Validate user expense details and
    income details within 25 chracters
    returns:
        string
    """
    while True:
        user_input = input(text)
        if len(user_input) == 0:
            print()
            print(RED + "Details cannot be empty" + RESET)
            print(RED + "Please enter details within"
                  f" {max_len} characters.\n" + RESET)
            print()
        elif len(user_input) > max_len:
            print()
            print(RED + "Text is too long" + RESET)
            print(RED + "Please enter the details within"
                  f" {max_len} characters." + RESET)
            print()
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
    returns:
        None
    print the updated data in the worksheet
    """
    print()
    print(YELLOW + "Updating datas in"
          f" {worksheet_name} worksheet........\n" + RESET)
    print()
    worksheet = SHEET.worksheet(worksheet_name)

    if worksheet_name == "Expenses":
        data_list = [data.amount, data.category, data.details, data.date_time]
    elif worksheet_name == "Income":
        data_list = [data.source, data.income_amount, data.date_time]
    else:
        print(RED + "Invalid worksheet,"
              " Please enter a valid worksheet name" + RESET)
        return

    worksheet.append_row(data_list)
    print(RED + f"{worksheet_name} worksheet updated successfully" + RESET)
    print()
    print(data)


def show_datas(worksheetname):
    """
    Shows the datas in the worksheet
    in a table format
    """
    worksheet = SHEET.worksheet(worksheetname)
    all_datas = worksheet.get_all_values()

    if worksheetname == "Expenses":
        if len(all_datas) <= 1:
            print(RED + "No expense data available" + RESET)
        else:
            print()
            print("===================================")
            print(CYAN + "     EXPENSE DATAS RECORD" + RESET)
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
            print(RED + "No Income data available" + RESET)
        else:
            print()
            print("=====================================")
            print(CYAN + "     INCOME DATAS RECORD" + RESET)
            print("=====================================")
            print()
            print(f"{'Itm_No':9} {'Income Type':<25}"
                  f"{'Actual Income':<15} {'Date/Time':^30}")
            print("-"*80)
            income_item = 0
            for row in all_datas[1:]:
                # looping to get all the row values form google sheet
                print(f"{(income_item+1):^9} {row[0]:<25}"
                      f"{row[1]:^15} {row[2]:^30}")
                print()
                income_item += 1
    else:
        pass


def summarize_expenses():
    """
    Summarize expenses by category
    and compares it with the total income amount
    returns:
        None
    """
    worksheet = SHEET.worksheet("Expenses")
    all_expense_data = worksheet.get_all_values()
    if len(all_expense_data) <= 1:
        print(RED + "No expense data available" + RESET)
        print()
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
    print(CYAN + "  EXPENSE SUMMARY BY CATEGORY" + RESET)
    print("=================================")
    print()
    for category, total in sum_of_category.items():
        print(f"{category} : {YELLOW}{total}{RESET}")

    max_category = max(sum_of_category, key=sum_of_category.get)
    max_expense = sum_of_category[max_category]

    print()
    print("You spent the most in the category")
    print(f"{YELLOW}{max_category} {RESET}"
          f"with a total of {YELLOW}{max_expense}{RESET}"
          " euros.")
    print()
    # access through class method sum of income
    income = Income.sum_of_income()
    # access through class method sum of expense
    expense = Expense.sum_of_expense()
    balance_amount = income-expense
    if expense < balance_amount:
        print()
        print("You have balance of"
              f"{YELLOW} {balance_amount}{RESET} euros from your income")
        print()
    elif expense > balance_amount:
        print()
        print("You have deficit of "
              f"{YELLOW} {balance_amount}{RESET}euros from your income")
        print()
    else:
        print()
        print(YELLOW + "You have no balance from your income" + RESET)
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
            print(RED + "No expense data available" + RESET)
            print()
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
                    print(YELLOW + "Deleted item:" + RESET, item)
                    print()
                    break
                else:
                    print()
                    print(RED + "Invalid item."
                          " Please enter a valid item number.\n" + RESET)
                    print()
            except ValueError:
                print()
                print(RED + "Invalid Input,"
                      " Please enter a valid item from above table\n" + RESET)
                print()

    elif worksheetname == "Income":
        # Check if there are no data records except the header row
        if len(all_datas) <= 1:
            print(RED + "No income data available" + RESET)
            print()
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
                    print()
                    print(YELLOW + "Deleted item:" + RESET, item)
                    print()
                    break
                else:
                    print()
                    print(RED + "Invalid item."
                          "Please enter a valid item number.\n" + RESET)
                    print()
            except ValueError:
                print()
                print(RED + "Invaid Item,"
                      "Please enter a valid item number" + RESET)
                print()
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
            print(CYAN + "         WELCOME TO EXPENSIFY           " + RESET)
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
            user_input = int(input(BLUE + "Enter you choice[1-4]:\n" + RESET))
            print()
            if user_input == 1:
                income_menu_option()
            elif user_input == 2:
                expense_menu_options()
            elif user_input == 3:
                help_menu()
            elif user_input == 4:
                print(GREEN + "EXITING FROM EXPENSIFY."
                      " HAVE A GOOD DAY" + RESET)
                print()
                break
            else:
                print()
                print(RED + "Invalid Option ,"
                      " Please enter a valid option from [1-4]" + RESET)
                print()
        except ValueError:
            print()
            print(RED + "Invalid Input ,"
                  " Please enter a number from (1-4)" + RESET)
            print()
        except KeyboardInterrupt:
            print()
            print(RED + "[91m\nKeyboard interruption"
                  " detected. Exiting..." + RESET)
            print()
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
        print(CYAN + "    MANAGE INCOME MENU       " + RESET)
        print("===========================")
        print()

        for opt, options in enumerate(income_options, 1):
            print(f"{opt}.{options}")
        try:
            value_range = f"[1-{len(income_options)}]"
            print()
            selected_index = int(input(BLUE + "Select an option from"
                                       f"{value_range}:\n" + RESET))
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
                    print(GREEN + "Returning to main menu..........." + RESET)
                    print()
                    break
                else:
                    print()
                    print(RED + "Invalid option" + RESET)
                    print(RED + "Please enter a"
                          f" valid option from {value_range}" + RESET)
                    print()
            else:
                print()
                print(RED + "Invalid option" + RESET)
                print(RED + "Please enter a valid"
                      f" option from {value_range}" + RESET)
                print()

        except KeyboardInterrupt:
            print()
            print(RED + "\nKeyboard interruption detected."
                  "Returning to Main Menu..." + RESET)
            print()
            break
        except ValueError:
            print()
            print(RED + "Invalid Input ,"
                  f" Please enter a number from {value_range}" + RESET)
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
        print(CYAN + "   MANAGE EXPENSES MENU    " + RESET)
        print("===========================")
        print()
        # looping to number the options
        for opt, option in enumerate(options, 1):
            print(f"{opt}.{option}")
        try:
            value_range = f"[1-{len(options)}]"
            print()
            user_choice = int(input(BLUE + "Select an option"
                                    f" from {value_range}:\n" + RESET))
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
                    print(GREEN + "Returning to main menu....." + RESET)
                    print()
                    break
                else:
                    print()
                    print(RED + "Invalid option," + RESET)
                    print(RED + "Please enter a"
                          f" valid option from {value_range}" + RESET)
                    print()
            else:
                print()
                print(RED + "Invalid option," + RESET)
                print(RED + "Please enter a"
                      f" valid option from {value_range}" + RESET)
                print()
        except KeyboardInterrupt:
            print()
            print(RED + "\nKeyboard interruption detected."
                  " Returning to Main Menu..." + RESET)
            print()
            break
        except ValueError:
            print()
            print(RED + "Invalid Input ,"
                  f" Please enter a number from {value_range}" + RESET)
            print()


def help_menu():
    """
    Printing the help menu
    """
    print(CYAN + "EXPENSIFY:Your Personal Expense Tracker" + RESET)
    print("-------------------------------------------"
          "------------------------------------")
    print("Expensify is a handy tool designed to\n\n"
          "help you manage your expenses efficiently.\n\n"
          "With Expensify, you can easily track your spending,\n\n"
          "record your income, and categorize your transactions \n\n"
          "to gain insights into your financial habits. \n\n")
    print(CYAN + "Manage Expenses Menu:" + RESET)
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
    print(CYAN + "Manage Income Menu:" + RESET)
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
    print(CYAN + "Instructions:" + RESET)
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
