
# Personal Expense Tracker

## Project Overview

The **Personal Expense Tracker** is a Python-based application designed to help users keep track of their personal expenses. The application allows users to record, categorize, and analyze their spending habits, providing valuable insights through data visualization.

## Objectives

- Develop a Python application to manage personal expenses.
- Record and categorize expenses such as Food, Travel, Bills, etc.
- Save expense data to a file for persistence.
- Analyze expenses to provide summaries by category.
- Visualize spending patterns using data visualization techniques.

## Project Phases

### Phase 1: Understanding Requirements and Basic Design
- Define key features: adding expenses, viewing expenses, and generating reports.
- Design the program flow and outline core functions.

### Phase 2: Implement Core Functionality
- **Tasks:**
  - Create functions to add and view expenses.
  - Implement code for basic operations like recording and displaying expenses.

### Phase 3: Data Storage and Retrieval
- Save expenses to a CSV file and load them when the application starts.
- Ensure data persistence between sessions.

### Phase 4: Data Analysis and Visualization
- Implement basic data analysis to summarize expenses by category.
- Use Matplotlib to visualize spending patterns.

### Phase 5: Testing and Debugging
- Test each function individually for accuracy.
- Handle errors like incorrect input formats and file issues.

## Key Features

- **Add Expenses:** Allows users to add details such as amount, date, category, and description.
- **View Expenses:** Displays all recorded expenses.
- **Save and Load Data:** Saves expenses to a CSV file for easy retrieval.
- **Analyze and Visualize:** Provides summaries and visual representations of spending habits.

## Code Snippets

### Adding an Expense

```python
expenses = []  # List to store expense entries

def add_expense():
    amount = float(input("Enter the expense amount: "))
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel): ")
    description = input("Enter a brief description: ")

    expense = {
        'amount': amount,
        'date': date,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")
```

### Viewing Expenses

```python
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAll Recorded Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. Amount: {expense['amount']}, Date: {expense['date']}, "
              f"Category: {expense['category']}, Description: {expense['description']}")
    print()
```

## Installation

1. Clone the repository:
    ```bash
    git clone github.com/8870hack/Mainflow-tasks.git
    ```
2. Navigate to the project directory:
    ```bash
    cd personal-expense-tracker
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. Run the main Python file to start the application.
2. Use the menu to add, view, analyze, and save expenses.

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions.

## License

This project is licensed under the MIT License.

---

*Developed during a Python Developer Internship as a hands-on project to enhance coding skills and data analysis techniques.*
