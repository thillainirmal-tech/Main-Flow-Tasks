import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                      (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL, description TEXT)''')
    conn.commit()
    conn.close()

# Function to add expense to the database
def add_expense(date, category, amount, description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                   (date, category, amount, description))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Expense added successfully")

# Function to delete expense by ID
def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Expense deleted successfully")

# Function to fetch all expenses from the database
def fetch_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

# GUI setup
class ExpenseTracker:
    def _init_(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        
        # Date entry
        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD)")
        self.date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry