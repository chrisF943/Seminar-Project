import requests
import datetime

stock_url = "https://www.alphavantage.co/query"
stock_key = "WDK56JX91HXK0CQ1"

tickers = ["IBM", "AAPl", "MSFT", "GOOGL", "ORCL"]
values = []

for ticker in tickers:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": stock_key,
    }

    response = requests.get(stock_url, params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    most_recent_date = max(data.keys())
    close_value = data[most_recent_date]["4. close"]
    values.append(f"{ticker}: {float(close_value)}")
    print(f"{ticker}: {float(close_value)}")

today = datetime.datetime.now().strftime("%m/%d/%Y")

with open("/home/Chris943/stocks.txt", "a") as file:
    file.write(f"\n{today}\n")
    for value in values:
        file.write(f"{value}\n")
