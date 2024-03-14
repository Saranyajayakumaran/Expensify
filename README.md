# EXPENSIFY  

Expensify is a versatile expense tracker designed to help users manage their finances efficiently. With Expensify, users can effortlessly record their expenses, track income, and gain valuable insights into their spending habits. Whether you're budgeting for personal expenses, managing business finances, or simply looking to gain better control over your money, Expensify offers a user-friendly solution tailored to your needs.

## Technologies Used

- Python
     - Programming language used for project development.

- Vs code:
    - Visual studio code IDE is used to write ,edit and debug python code.

- Google sheet
    - Google sheet is  a cloud Api used to store and edit datas.

- GitHub
    - GitHub is a Version control system for managing codebase and collaboration.

- Git
    - Git is used to tracking changes and managing branches from the development Interface.

- Heroku
    - Cloud platform used for deployment and hosting of the application.


# Features

## Existing Features

### Main menu

  - The main menu of Expensify provides users with a simple and intuitive interface to manage their income and expenses effectively. 
  - Upon launching the application, users are greeted with options to navigate between managing income and expenses, or exiting the application. 

    - Main menu options
        - Manage Income
        - Manage Expense
        - Help
        - Exit

    
### Manage Income
- The Manage income feature helps user to efficiently track and manage their source of income.
- When user selects the Manage Income optionfrom the main menu, users can seamlessly record new income entries by providing details such as the income amount, its source, and any relevant additional information. 
   
   - Options in manage income
        - Record new Income
        - view all Income
        - Delete Income
        - Return to main menu

    - Record a new income: 
            Enable users to input their income details, including the amount, source, and date/time.
    - View all income: 
            Display a summary of all recorded income entries, including the item number, amount, source, and date/time.
    - Delete income: 
            Allow users to remove a specific income entry by selecting the item number.
    - Return to main menu:
            Allow user to navigate back to main menu when they needed

### Manage Expense
- The Manage expense feature helps user to efficiently track and manage their expenses.
- When user selects the Manage Expense option from the main menu, users can seamlessly record new expense entries by providing details such as the expense amount, its category, and any relevant additional information. 
   
   - Options in manage expense
        - Record new Expense
        - view all Expense
        - Delete Expense
        - Return to main menu

    - Record a new expense: 
            Allow users to input their expenses, including the amount spent, category, and details.
    - View all expenses: 
            Display a summary of all recorded expenses, including the item number, amount, category, details, and date/time.
    - Summarize expenses: 
            Provide a breakdown of expenses by category and show the total amount spent in each category.
    - Delete expense: 
            Allow users to remove a specific expense entry by selecting the item number.

### Help
- The Help feature provides users with a simple and intuitive interface to access the Expensify app.

### Exit
- Exit feature allows user to exit the application.

## Future Implementation
- User Authentication and Account Management:
        Implement user authentication and account creation to maintain personal accounts.
- Budget and goal tracking:
        Introduce budgeting tools that allow user to set spending limits for different categories.
- Enable notifications:
        Enable notification when amount the total amount is reducing from income.
- Monthly spread sheeet:
        Enable monthls spreadsheet for every month to track the expense and income.
- Multi currency support:
        Add support for multiple currencies and exchange rate conversions to accomodate users who travel internationally.
- Mobile app enchancements:
        Develop a mobile app version of Expensify to enhance accessibility and convenience for users on the go. 


## How the App works:
- Step1: From the main menu user can select any one option manage income or manage expense.
- Step2: When user selects manage expense it contains 5 options
- Step3: if option1
                Record new expense
                        Enter the datas expense amount, select category, give details and it store in spread sheet with date and time.
         else if option2
                View all expense
                        User can see all the recorded expense in a table with all the details
         else if option3 
                Summrize Expense
                        User will see the breakdown of user expenses by category, it helps to understand your spending habits. 
         else if option 4
                Delete Expense
                        It helps the user to delete a row of datas from google sheet with item number from expeses worksheet which user selected.
         else if option 5
                Return to main menu
                        User can go back to main menu.
- Step 4: When user selects manage income from main menu it contains 4 options
- Step 5: if option 1
                Record new income
                        Enter the datas of income amount and its source and it store in spread sheet with date and time.
         else if option 2
                View all income
                        User can see all the recorded income in a table with all the details
         else if option 3 
                Delete income
                        It helps the user to delete a row of data from google sheet with the item number from income worksheet which user selected.
         else if option 4
                Return to main menu
                        User can go back to main menu.
- Step 6: When user selects help menu from main menu, It will show the overview of expensify app and show the informantion of each field and how to use it.
- Step 7: When user selects exit menu from main menu, It will close the app.

(The amount will be validate with 0 nd negative numbers nd also limited to 8 digits)
(The characters in message and details of income and expense are also limited to 25)

## Testing

                      

               
