from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert')
def convert():
    amount = request.args.get('amount', 1)
    from_currency = request.args.get('from', 'GBP').upper()
    to_currency = request.args.get('to', 'USD').upper()

    url = f"https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}"
    response = requests.get(url)
    data = response.json()

    rate = data.get('rates', {}).get(to_currency)
    if not rate:
        return jsonify({"error": "Conversion not available"})

    converted = float(amount) * rate

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "rate": rate,
        "amount": amount,
        "converted": round(converted, 2)
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)