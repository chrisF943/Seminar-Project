import os
import requests
import datetime

today = datetime.date.today()
day = today.weekday()


def get_prices():
    # Check if it is a weekday, if so then API is called, else message is printed
    if day < 5:
        # API endpoint and fetch key from env variable
        stock_url = "https://www.alphavantage.co/query"
        stock_key = os.environ.get("API_KEY")

        # Create list of tickers and list for prices
        tickers = ["AAPl", "MSFT", "GOOGL", "AMZN"]
        values = []
        # Calls API for each ticker
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
            # This API provides alot of data, so only the most recent date and close value is used
            if data:
                most_recent_date = max(data.keys())
                close_value = data[most_recent_date]["4. close"]
                values.append(f"{ticker}: {float(close_value)}")
                print(f"{ticker}: {float(close_value)}")

        write_data(values)

    # If it is not a weekday, message is printed
    else:
        print("It is not a weekday, market is closed.")


def write_data(values):
    # Converts date to mm/dd/yyyy format
    date = datetime.datetime.now().strftime("%m/%d/%Y")

    # Writes date and values to file for each ticker
    with open("/home/Chris943/stocks.txt", "a") as file:
        file.write(f"\n{date}\n")
        for value in values:
            file.write(f"{value}\n")


if __name__ == "__main__":
    get_prices()
