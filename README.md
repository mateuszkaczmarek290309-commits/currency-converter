# Currency Converter

A simple currency converter built with Python and Flask. Convert between major world currencies using live daily exchange rates.

## What it does

- Choose an amount and two currencies (from and to)
- Fetches the latest exchange rate from the Frankfurter API
- Shows a clear converted result, e.g. "10 GBP = 12.50 USD"

## Why I built it

I built this to practise working with external APIs and to have a clean, finance-relevant project for my CV alongside my other apps.

## Technologies used

- Python 3
- Flask
- Frankfurter API (free, no API key required)
- HTML/CSS/JavaScript

## How to run it

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests
python3 app.py
```

Open http://127.0.0.1:5002 in your browser.
