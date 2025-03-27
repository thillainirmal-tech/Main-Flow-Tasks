import sqlite3
import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Connect to the SQLite database and create tables
connection = sqlite3.connect('billing_app.db')
cursor = connection.cursor()

# Create tables for products, customers, and transactions
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    name TEXT,
                    price REAL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY,
                    name TEXT,
                    contact TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    total REAL,
                    date TEXT,
                    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY(product_id) REFERENCES products(product_id))''')
connection.commit()
print("Database tables created successfully!")

# Step 2: Function to add a product to the database
def add_product_to_db(name, price):
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    connection.commit()
    print(f"Product '{name}' added successfully with price {price}.")

# Step 3: Function to add a customer to the database
def add_customer_to_db(name, contact):
    cursor.execute("INSERT INTO customers (name, contact) VALUES (?, ?)", (name, contact))
    connection.commit()
    print(f"Customer '{name}' added successfully with contact '{contact}'.")

# Step 4: Function to generate a PDF invoice
def generate_invoice(transaction_id, customer_name, items):
    pdf_path = f"Invoice_{transaction_id}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"Invoice for {customer_name}")

    y = 700  # Starting position for item list
    for item in items:
        c.drawString(100, y, f"{item['name']} - Qty: {item['quantity']} - Price: {item['price']}")
        y -= 20

    c.showPage()
    c.save()
    print(f"Invoice saved as '{pdf_path}'")

# Step 5: GUI for Adding Products
def open_product_entry_form():
    # Initialize the window
    product_window = tk.Tk()
    product_window.title("Add Product")
    
    # Labels and Entry widgets for product name and price
    tk.Label(product_window, text="Product Name:").grid(row=0, column=0)
    tk.Label(product_window, text="Price:").grid(row=1, column=0)
    
    name_entry = tk.Entry(product_window)
    price_entry = tk.Entry(product_window)
    name_entry.grid(row=0, column=1)
    price_entry.grid(row=1, column=1)

    # Save product function to add the product to the database
    def save_product():
        name = name_entry.get()
        try:
            price = float(price_entry.get())
            add_product_to_db(name, price)
            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
            product_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price.")

    # Save Button
    save_button = tk.Button(product_window, text="Save Product", command=save_product)
    save_button.grid(row=2, column=1)

    # Run the window
    product_window.mainloop()

# Run the product entry form GUI
open_product_entry_form()