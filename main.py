import os
import requests
import datetime

today = datetime.date.today()
day = today.weekday()

stock_url = "https://www.alphavantage.co/query"
stock_key = os.environ.get("API_KEY")

tickers = ["AAPl", "MSFT", "GOOGL", "AMZN"]
values = []

if day < 5:
    for ticker in tickers:
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": ticker,
            "apikey": stock_key,
        }

        response = requests.get(stock_url, params)
        response.raise_for_status()
        try:
            data = response.json()["Time Series (Daily)"]
        except KeyError as e:
            print(f"API Error: {e}")
            print(response.json())
            data = None
        if data:
            most_recent_date = max(data.keys())
            close_value = data[most_recent_date]["4. close"]
            values.append(f"{ticker}: {float(close_value)}")
            print(f"{ticker}: {float(close_value)}")

    date = datetime.datetime.now().strftime("%m/%d/%Y")

    with open("/home/Chris943/stocks.txt", "a") as file:
        file.write(f"\n{date}\n")
        for value in values:
            file.write(f"{value}\n")

else:
    print("It is not a weekday, market is closed.")
