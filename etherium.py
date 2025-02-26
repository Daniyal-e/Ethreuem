from flask import Flask, jsonify
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow React to fetch data

# Function to fetch Ethereum price history (Last 30 days)
def get_eth_price():
    eth = yf.Ticker("ETH-USD")
    data = eth.history(period="30d")  
    prices = data['Close'].to_dict()
    return prices

# API Route to get Ethereum price history
@app.route('/api/eth-price', methods=['GET'])
def eth_price():
    try:
        prices = get_eth_price()
        return jsonify({"prices": prices})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)