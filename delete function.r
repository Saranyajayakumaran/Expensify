def show_expense_data():
    """
    #Show all the expenses to the user in table
    """
    worksheet=SHEET.worksheet("Expenses")
    all_expense_data=worksheet.get_all_values()
    if len(all_expense_data)==0:
        print("No expense data available")
    else:
        print(f"Expense datas record :")
        print("{:15} {:<15} {:<15} {:<35} {:<20}".format("ItemNumber","Amount(euro)","Category","Details","Date/Time"))
        print("-"*100)

        item = 0
        for row in all_expense_data[1:]: # looping to get all the row values form google sheet
            print("{:^15}  {:<15} {:<15} {:<35} {:<20}".format(item+1, *row))
            item += 1

def show_income_data():
    """
    #Show all the Incomes to the user in table
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
