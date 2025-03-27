<<<<<<< HEAD
# 💵 USD Currency Converter

A simple Python-based USD currency converter application with a graphical user interface (GUI) that allows users to convert USD to various other currencies based on the latest exchange rates. The application fetches live rates from an API and performs real-time conversions.

---

## 📌 **Project Overview**

- **Language:** Python  
- **Libraries Used:**  
  - `Tkinter` (for GUI)  
  - `Requests` (for API calls)  
- **API Used:** [ExchangeRate-API](https://www.exchangerate-api.com)  

---

## ⚙️ **Features**

✅ **Real-Time Conversion:** Fetches live conversion rates from USD to multiple currencies.  
✅ **User-Friendly Interface:** Allows easy input of amounts in USD and selection of target currencies.  
✅ **Accurate Results:** Handles various input cases for reliable currency conversions.  

---

## 🚀 **Installation**

### 🛠️ Prerequisites

- Python 3.x installed  
- (Optional) Jupyter Lab (for GUI interface)  
- ExchangeRate-API key (available at [ExchangeRate-API](https://www.exchangerate-api.com))  

### 🔧 **Setup Instructions**

1. **Clone the repository:**
```bash
git clone https://github.com/thillainirmal-tech/USD-Currency-Converter.git
cd USD-Currency-Converter
```

2. **Install the required Python libraries:**
```bash
pip install requests
```

3. **Add your API key:**
- Open `currency_converter.py`
- Replace `YOUR_API_KEY` with your actual ExchangeRate-API key in the `fetch_rates()` function:
```python
url = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"
```

---

## 💡 **Usage**

1. **Run the Application:**
```bash
python currency_converter.py
```

2. **Instructions:**
- Enter an amount in USD in the input field.  
- Select the target currency from the dropdown menu.  
- Click the **"Convert"** button to see the conversion result.  

---

## 🛠️ **Code Overview**

```python
import requests
import tkinter as tk

def fetch_rates():
    url = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']

def convert():
    try:
        usd_amount = float(entry.get())
        target_currency = currency_var.get()
        rate = rates.get(target_currency)
        if rate:
            converted_amount = usd_amount * rate
            result_label.config(text=f"{usd_amount} USD = {converted_amount:.2f} {target_currency}")
        else:
            result_label.config(text="Invalid currency selection.")
    except ValueError:
        result_label.config(text="Invalid USD amount.")

# GUI Configuration
root = tk.Tk()
root.title("USD Currency Converter")

entry_label = tk.Label(root, text="Enter amount in USD:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

rates = fetch_rates()
currency_var = tk.StringVar(root)
currency_var.set("EUR")
currency_menu = tk.OptionMenu(root, currency_var, *rates.keys())
currency_menu.pack()

result_label = tk.Label(root, text="Result will appear here")
result_label.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

root.mainloop()
```

---

## 📚 **Contributing**
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.  

---

## 📜 **License**
This project is licensed under the MIT License.  

=======
# Billing Software Application

A simple billing software application developed in Python, featuring a graphical user interface (GUI) for managing customer transactions, generating invoices, and tracking sales. The application uses [...]

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Download](#download)
- [Contributing](#contributing)
- [License](#license)

## Features
- Add and manage product details (name, price).
- Add and manage customer information (name, contact).
- Generate PDF invoices for customer transactions.
- Simple and user-friendly GUI using Tkinter.

## Requirements
- Python 3.x
- SQLite3 (comes with Python)
- Tkinter (comes with Python on most systems)
- [ReportLab](https://www.reportlab.com/) for PDF generation

To install the ReportLab library, use:
```bash
pip install reportlab
>>>>>>> bill-generation-branch
