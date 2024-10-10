import datetime

start_date = datetime.date(2023, 9, 5)
end_date = datetime.date(2023, 11, 2)

tickers = ["AAPL:", "MSFT:", "GOOGL:", "AMZN:"]

with open("/Users/chrisfaris/Desktop/historical_data.txt", "a") as f:
    for date in range(int((end_date - start_date).days) + 1):
        current_date = start_date + datetime.timedelta(days=date)
        f.write(current_date.strftime("%m/%d/%y") + "\n")
        for ticker in tickers:
            f.write(ticker + "\n")
        f.write("\n")
