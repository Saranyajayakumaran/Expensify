# EXPENSIFY  

Expensify is a versatile expense tracker designed to help users manage their finances efficiently. With Expensify, users can effortlessly record their expenses, track income, and gain valuable insights into their spending habits. Whether you're budgeting for personal expenses, managing business finances, or simply looking to gain better control over your money, Expensify offers a user-friendly solution tailored to your needs.

Have a look at the project by clicking the link below:
https://expense-track-77e4d822539c.herokuapp.com/


![Tite page](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/title%20page.png)

## Technologies Used

- Python
     - Programming language used for project development.

- VS code:
    - Visual studio code IDE is used to write ,edit and debug python code.

- Google sheet
    - Google sheet is  a cloud API used to store and edit datas.

- GitHub
    - GitHub is a Version control system for managing codebase and collaboration.

- Git
    - Git is used to tracking changes and managing branches from the development interface.

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

![Manage Income](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/manage%20income%20.png)

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
            The category allows to select from 5 options Food, Home, Car, Fun, Misc
    - View all expenses: 
            Display a summary of all recorded expenses, including the item number, amount, category, details, and date/time.
    - Summarize expenses: 
            Provide a breakdown of expenses by category and show the total amount spent in each category.
    - Delete expense: 
            Allow users to remove a specific expense entry by selecting the item number.

![Manage Expense](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/manage%20expense%20.png)

### Help
- The Help feature provides users with a simple and intuitive interface to access the Expensify app.

![Help Menu](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/Help%20menu.png)

### Exit
- Exit feature allows user to exit the application.

## Future Implementation

- User Authentication and Account Management:
        Implement user authentication and account creation to maintain personal accounts.
- Budget and goal tracking:
        Introduce budgeting tools that allow user to set spending limits for different categories.
- Enable notifications:
        Enable notification when the expense amount is more than income.
- Monthly spread sheeet:
        Enable monthly spreadsheet for every month to track the expense and income.
- Multi currency support:
        Add support for multiple currencies and exchange rate conversions to accomodate users who travel internationally.
- Mobile app enchancements:
        Develop a mobile app version of Expensify to enhance accessibility and convenience for users on the go. 

## How to Use Expensify

### Step 1: Selecting Options from the Main Menu
- From the main menu, users can choose to manage income or manage expenses.

### Step 2: Managing Income 
- Alternatively, users can choose to manage income, which presents similar options for recording, viewing, summarizing, and deleting income data.
   **Record New Income:**
      - Users can enter the income amount, specify its source, and store the data in the spreadsheet along with the date and time.
   **View All Income:**
      - Users can view all recorded income entries in a table with detailed information.

  ![view income record](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/income%20data.png)
  
   **Delete Income:**
      - Allows users to delete a specific income entry by selecting its item number from the income worksheet.
   **Return to Main Menu:**
      - Provides an option to return to the main menu for further navigation.

### Step 3: Managing Expenses
- When selecting "Manage Expenses," users are presented with five options:
   **Record New Expense:**
      - Users can enter the expense amount, select a category, provide details, and store the data in the spreadsheet along with the date and time.
   **View All Expenses:**
      - Users can view all recorded expenses in a table with detailed information.

![View expense record](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/expense%20data%20record.png)

   **Summarize Expenses:**
      - Users can see a breakdown of their expenses by category, helping them understand their spending habits.

![Expense Summary](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/summerize%20expense.png)

   **Delete Expense:**
      - Allows users to delete a specific expense by selecting its item number from the expenses worksheet.
   **Return to Main Menu:**
      - Provides an option to return to the main menu for further navigation.

### Step 4: Accessing Help
- Users can access the help menu from the main menu to get an overview of the Expensify app and learn how to use its features effectively.

### Step 5: Exiting the App
- Users can choose the exit option from the main menu to close the Expensify app.


## Flow Chart : How the project works

![Flow chart](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/flowchart.png)

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

I have validated our codebase using PEP8 to ensure adherence to Python's coding standards. Below is a screenshot demonstrating the PEP8 validation process for our project:

![pylint screenshot](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/screen%20shot%20pep8.png)

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
|ctrl+c|Application should exit with interruption |Pass|


### MANAGE INCOME MENU

#### Valid Input Handling

|User Input|Expected Behavior|Pass/Fail|
|----------|-----------------|----------|
|Enter 1|Successfully navigate to Record new income|Pass|
|Enter 2|Successfully navigate to View all income|Pass|
|Enter 3|Successfully navigate to Delete income data|Pass|
|Enter 4|Successfully navigate to Main menu|Pass|

#### Invalid Input Handling

|User Input|Expected Behavior|Pass/Fail|
|----------|-----------------|----------|
|Enter 0|Prompt user to re-enter a valid option|Pass|
|Enter value > 4|Prompt user to re-enter a valid option|Pass|
|Enter a string/char|Prompt user to re-enter a valid numeric option|Pass|
|ctrl+c|Application should go to main neu with interruption|Pass|

##### Record new income data

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|---------|
|Amount(int)|Enter amount|store in google sheet|Pass|
|Amount(float)|Enter amount |Store in google sheet|Pass|
|Details|Enter details|Store in googl sheeet|Pass|
|Date/time|Current date/time|Store current date time in google sheet|Pass|

##### Invalid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|---------|
|Amount|Enter 0|Prompt user to re-enter a valid option|Pass|
|Amount|Enter>8 digit|Prompt user to re-enter a valid option|Pass|
|Amount|Enter negative|Prompt user to re-enter a valid option|Pass|
|Amount|Enter string|Prompt user to re-enter a valid option|Pass|
|Details|string>25|Prompt user to re-enter a valid option|Pass|
|Details|Empty|Prompt user to re-enter a valid option|Pass|


##### View all income data

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|No datas in google sheet |Enter 2|Error:No data available in google sheet|Pass|
|Datas in google sheet|Enter 2|Display all data in google sheet|Pass|


#### Delete income data

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|No datas in google sheet |Enter 3|Error:No data available in google sheet|Pass|
|Data available in google sheet|Enter 3|Display all data in Google Sheet and prompt user to enter item number to delete|Pass|
|Item number available|enter item number|Delete the specified item|Pass|

##### Invalid Input Handling
|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|Case 1|Enter a number not available|Error:No data available in google sheet|Pass|
|case 2|Enter a string/char|Error:invalid input|Pass|

### MANAGE EXPENSE MENU

#### Record New Expense 

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|Amount(int)|Enter amount|store in google sheet|Pass|
|Amount(float)|Enter amount |Store in google sheet|Pass|
|Category|select 1-5|store in gogole sheet|Pass|
|Details|Enter details within 25 char|Store in Google sheet|Pass|

##### Invalid Input Handling

|Test Case|User Input|Expected Behavior|Passs/Fail|
|---------|----------|-----------------|----------|
|Amount|Enter 0|Prompt user to re-enter a valid option|Pass|
|Amount|Enter>8 digit|Prompt user to re-enter a valid option|Pass|
|Amount|Enter negative|Prompt user to re-enter a valid option|Pass|
|Amount|Enter string|Prompt user to re-enter a valid option|Pass|
|Category|Enter 0|Prompt user to re-enter a valid option|Pass|
|Category|Enter >5|Prompt user to re-enter a valid option|Pass|
|Category|Enter a string/char|Prompt user to re-enter a valid option|Pass|
|Details|string>25|Prompt user to re-enter a valid option|Pass|
|Details|Empty|Prompt user to re-enter a valid option|Pass|

##### View all Expense data

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|No datas in google sheet |Enter 2|Error:No data available in google sheet|Pass|
|Datas in google sheet|Enter 2|Display all data in google sheet|Pass|

#### Delete Expense data

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|No datas in google sheet |Enter 3|Error:No data available in google sheet|Pass|
|Data available in google sheet|Enter 3|Display all data in Google Sheet and prompt user to enter item number to delete|Pass|
|Item number available|enter item number|Delete the specified item|Pass|

##### Invalid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|Case 1|Enter a number not available|Error:No data available in google sheet|Pass|
|case 2|Enter a string/char|Error:invalid input|Pass|


#### Summerize Expenses

##### Valid Input Handling

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|No datas in google sheet|Enter 4|Error:No data available in google sheet|Pass|
|Datas in google sheet|Enter 4|Display all data in google sheet|Pass|


### Help menu

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|Case 1 |Enter 4|Display Help Menu|Pass|

### Exit

|Test Case|User Input|Expected Behavior|Pass/Fail|
|---------|----------|-----------------|----------|
|Case 1 |Enter 5|Exit the application|Pass|


### Fixed Bugs

|Bugs Found|Expectation|How i solved it|
|----------|----------|---------------|
|Handling Empty Data|it should display "No data available"| Add checks to handle cases where the user doesn't input any data.|     
|Incorrect Printing of Data|it should print data in a table format|Ensure that data is printed correctly, especially when formatting table-like outputs.
|Error Handling for Invalid Input|should show error message |Add error handling to handle cases where the user inputs invalid data or selections.| 
|Getting all the digits in amount|it should accept only 8 digits|Add checks to handle cases where the user inputs more than 8 digits.|
|Handling numeric data|It should not accept string data|Add checks to handle cases where the user inputs non-numeric data.| 

### Unfixed Bugs 

1. Currently, the code accepts any number of decimal points within a total of 8 digits.
2. The code allows for the acceptance of all alphabets and special characters in the details and source code fields. 

These bugs will be fixed in future.


## Lighthouse Validation

![Lighthouse validation](https://github.com/Saranyajayakumaran/Expensify/blob/main/images/light%20house%20validation.png)


### Deployment

The app was deployed through Heroku. The steps are as following:

- **Log into Github and locate Github Repository.**
- **Create a Heroku Account:**
  - If you haven't already, sign up for a Heroku account at Heroku's website.
- **Create a New Heroku App:**
  - Log into your Heroku account.
  - From the Heroku dashboard, click on the "New" button to create a new app.
  - Choose a unique name for your app.
  - Select the region closest to your location.
  - Click "Create app" to finalize the creation.
- **Configure App Settings:**
  - Go to your newly created app's settings.
  - Navigate to the "Config Vars" section.
  - Add any necessary environment variables that your application requires.
  - Ensure that you have configured the necessary buildpacks for your application.
- **Deploy Your Application:**
  - Scroll down to the "Deployment Method" section on your app's dashboard.
  - Select GitHub as the deployment method.
  - Connect your Heroku app to your GitHub repository by searching for and selecting the repository name.
  - Optionally, enable automatic deployment if you want your Heroku app to update automatically whenever changes are pushed to the connected GitHub repository.
  - Click the "Deploy Branch" button to manually deploy your application for the first time.


### Credits

- I would thank many sources and people who spported to complete my project.
     - Thank my mentor Dick vlaanderen who guided me and his ideas and corrections was very helpful.
     - The idea of the project has beenn referred from Youtube Channel [pixegami](https://www.youtube.com/watch?v=HTD86h69PtE&list=PLUuWC4-foh23z65szhmk0sord5-JdGUq7&index=1)
     - The detailed classes and methods are learned from the youtube channel [Error makes clever](https://www.youtube.com/watch?v=BVIoAILnZ4Q&list=PLvepBxfiuao1hO1vPOskQ1X4dbjGXF9bm)
     - W3schools and stackoverflow plays a major role in learning the concepts.
     - Google sheet concepts,saving datas to google sheet and heroku deployments are learned from [Love Sandwich](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/  293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=last)






