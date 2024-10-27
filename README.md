USD Currency Converter

A simple Python-based USD currency converter application with a graphical user interface (GUI) that allows users to convert USD to various other currencies based on the latest exchange rates. The application fetches live rates from an API and performs real-time conversions.

Project Overview

Language: Python

Libraries Used: Tkinter (for GUI), Requests (for API calls)

API Used: ExchangeRate-API


Features

Real-Time Conversion: Fetches live conversion rates from USD to multiple currencies.

User-Friendly Interface: Allows easy input of amounts in USD and selection of target currencies.

Accurate Results: Handles various input cases for reliable currency conversions.


Installation

Prerequisites

Python 3.x or jupyter lab(for gui interface)

ExchangeRate-API key (available at ExchangeRate-API)


Setup Instructions

1. Clone the repository:

git clone https://github.com/8870hack/USD-Currency-Converter.git
cd USD-Currency-Converter


2. Install the required Python libraries:

pip install requests


3. Add your API key:

Open currency_converter.py and replace YOUR_API_KEY in the fetch_rates() function:

url = "https://v6.exchangerate-api.com/v6/e95a18d93e37e78f9875c5ad/latest/USD"




Usage

1. Run the Application:

python currency_converter.py


2. Instructions:

Enter an amount in USD in the input field.

Select the target currency from the dropdown menu.

Click the "Convert" button to see the conversion result.




Code Overview

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

License

This project is open-source and available under the MIT License.
