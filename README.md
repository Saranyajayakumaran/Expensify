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

## How to Use Expensify

### Step 1: Selecting Options from the Main Menu
- From the main menu, users can choose to manage income or manage expenses.

### Step 2: Managing Expenses
- When selecting "Manage Expenses," users are presented with five options:
  1. **Record New Expense:**
      - Users can enter the expense amount, select a category, provide details, and store the data in the spreadsheet along with the date and time.
  2. **View All Expenses:**
      - Users can view all recorded expenses in a table with detailed information.
  3. **Summarize Expenses:**
      - Users can see a breakdown of their expenses by category, helping them understand their spending habits.
  4. **Delete Expense:**
      - Allows users to delete a specific expense by selecting its item number from the expenses worksheet.
  5. **Return to Main Menu:**
      - Provides an option to return to the main menu for further navigation.

### Step 3: Managing Income (Optional)
- Alternatively, users can choose to manage income, which presents similar options for recording, viewing, summarizing, and deleting income data.
  1. **Record New Income:**
      - Users can enter the income amount, specify its source, and store the data in the spreadsheet along with the date and time.
  2. **View All Income:**
      - Users can view all recorded income entries in a table with detailed information.
  3. **Delete Income:**
      - Allows users to delete a specific income entry by selecting its item number from the income worksheet.
  4. **Return to Main Menu:**
      - Provides an option to return to the main menu for further navigation.

### Step 4: Accessing Help
- Users can access the help menu from the main menu to get an overview of the Expensify app and learn how to use its features effectively.

### Step 5: Exiting the App
- Users can choose the exit option from the main menu to close the Expensify app.


## Validation Rules and Limits

### Amount Validation
- The amount entered for both income and expense entries is validated to ensure it meets the following criteria:
  - It cannot be zero.
  - It cannot be a negative number.
  - It is limited to a maximum of 8 digits.

### Message and Details Character Limit
- When providing details or messages for income and expense entries, users are required to adhere to the following character limits:
  - Messages and details are limited to a maximum of 25 characters.

## Options Validation

### Input Format
- When selecting options within the Expensify app, users must provide numeric input.
  - Options cannot be strings and must be numbers.
  - The input must be within the specified range of available options.
    - It cannot be zero.
    - It cannot exceed the maximum number of available options.

These validation rules ensure that users provide valid input when navigating the menu options in the Expensify app.

## Testing

## Functional testing

### MAIN MENU
#### Valid Input Handling

|User Input|Expected Behavior|Pass/Fail|
|------|---------------------|---------|
|Enter 1 |Successfully navigate to Manage Income|Pass|
|Enter 2 |Successfully navigate to Manage Expense|Pass|
|Enter 3|Successfully navigate to Help menu|Pass|
|Enter 4 |Successfully exit the application|Pass|


#### Invalid Input Handling
|User Input|Expected Behavior|Pass/Fail|
|----------|-----------------|---------|
|Enter 0|Prompt user to re-enter a valid option|Pass|
|Enter value > 4|Prompt user to re-enter a valid option|Pass|
|Enter a string/char|Prompt user to re-enter a valid numeric option|Pass|


### MANAGE INCOME

|User Input|Expected Behavior|Pass/Fail||pass|
|------|---------------|






               
