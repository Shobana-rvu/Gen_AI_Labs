import requests
import yfinance as yf

def get_currency(country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    data = requests.get(url, timeout=10).json()
    if not data or not isinstance(data, list):
        return "N/A", "N/A"
    currencies = data[0].get("currencies", {})
    if not currencies:
        return "N/A", "N/A"
    code = list(currencies.keys())[0]
    name = currencies[code]["name"]
    return code, name


def get_exchange_rates(base):
    try:
        url = f"https://open.er-api.com/v6/latest/{base}"
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return {"USD": "N/A", "INR": "N/A", "GBP": "N/A", "EUR": "N/A"}
        data = response.json()
        rates = data.get("rates", {})
        return {
            "USD": rates.get("USD", "N/A"),
            "INR": rates.get("INR", "N/A"),
            "GBP": rates.get("GBP", "N/A"),
            "EUR": rates.get("EUR", "N/A")
        }
    except:
        return {"USD": "N/A", "INR": "N/A", "GBP": "N/A", "EUR": "N/A"}


def get_index_value(symbol):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="1d")
    if hist.empty:
        return "N/A"
    return round(hist["Close"].iloc[-1], 2)