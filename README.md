Billing Software Application

A simple billing software application developed in Python, featuring a graphical user interface (GUI) for managing customer transactions, generating invoices, and tracking sales. The application uses SQLite for storing product, customer, and transaction data, and generates invoices in PDF format.

Table of Contents

Features

Requirements

Installation

Usage

Project Structure

Download

Contributing

License


Features

Add and manage product details (name, price).

Add and manage customer information (name, contact).

Generate PDF invoices for customer transactions.

Simple and user-friendly GUI using Tkinter.


Requirements

Python 3.x

SQLite3 (comes with Python)

Tkinter (comes with Python on most systems)

ReportLab for PDF generation


To install the ReportLab library, use:

pip install reportlab

Installation

1. Clone or download the repository:

git clone https://github.com/8870hack/Mainflow-tasks-bill_generation.git
cd Mainflow-tasks-bill_generation


2. Install dependencies (if not already installed):

pip install reportlab



Usage

1. Run the application: Open the script in your Python environment (IDLE, VSCode, etc.) and run it.

python billing_app.py


2. Add Products: A GUI window will appear allowing you to add products by entering their name and price.


3. Generate Invoice:

Modify the generate_invoice() function call at the bottom of the script with the relevant customer and item details.

Run the script again to generate a PDF invoice.



4. Check the Database: The billing_app.db SQLite database will be created in the project directory to store product, customer, and transaction data.



Project Structure

Mainflow-tasks-bill_generation/
├── billing_app.py       # Main application code
├── billing_app.db       # SQLite database (generated automatically)
└── Invoice_x.pdf        # Generated invoice PDF (sample file)

Download

To download the project directly, use the link below:

Download Billing Software Application

Alternatively, you can clone the repository by running:

git clone https://github.com/8870hack/Mainflow-tasks-bill_generation.git

Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or suggestions.

License

This project is licensed under the MIT License. See the LICENSE file for details.
