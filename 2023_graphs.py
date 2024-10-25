import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter
from datetime import datetime

# Initialize empty lists to hold the data
dates = []
aapl_prices = []
msft_prices = []
googl_prices = []
amzn_prices = []

# Open and read the file
with open("/Users/chrisfaris/Desktop/python/Seminar Project/2023_data.txt", "r") as file:
    lines = file.readlines()
    current_date = None

    # Iterate through each line
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line:  # Check if the line is not empty
            # Check if the line is a date (format: MM/DD/YYYY)
            try:
                current_date = datetime.strptime(line, '%m/%d/%Y')
                dates.append(current_date)  # Add the date to the list
            except ValueError:
                # If it's not a date, it's ticker data (e.g., "AAPL: 189.46")
                if 'AAPL' in line:
                    aapl_prices.append(float(line.split(': ')[1]))
                elif 'MSFT' in line:
                    msft_prices.append(float(line.split(': ')[1]))
                elif 'GOOGL' in line:
                    googl_prices.append(float(line.split(': ')[1]))
                elif 'AMZN' in line:
                    amzn_prices.append(float(line.split(': ')[1]))

# Create a pandas DataFrame with the parsed data
df = pd.DataFrame({
    'Date': dates,
    'AAPL': aapl_prices,
    'MSFT': msft_prices,
    'GOOGL': googl_prices,
    'AMZN': amzn_prices
})

# Set the 'Date' column as a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Set the figure size
plt.figure(figsize=(10, 6))

# Plot each ticker's price
plt.plot(df['Date'], df['AAPL'], label='AAPL', color='blue', linewidth=2)
plt.plot(df['Date'], df['MSFT'], label='MSFT', color='green', linewidth=2)
plt.plot(df['Date'], df['GOOGL'], label='GOOGL', color='red', linewidth=2)
plt.plot(df['Date'], df['AMZN'], label='AMZN', color='orange', linewidth=2)

# Formatting the date on the x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %d'))

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Ticker Price')
plt.title(' Closing Stock Prices for AAPL, MSFT, GOOGL, and AMZN (Sep 2023 - Nov 2023)')

# Add a legend to indicate which line represents which ticker
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Save the plot to a file
plt.savefig('graph.png', bbox_inches='tight')

# Show the plot
plt.tight_layout()
plt.show()

# Create individual graphs for each ticker

# Ticker symbols and corresponding colors
tickers = {
    'AAPL': 'blue',
    'MSFT': 'green',
    'GOOGL': 'red',
    'AMZN': 'orange'
}

# Create individual plots for each ticker
for ticker, color in tickers.items():
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df[ticker], label=ticker, color=color, linewidth=2)

    # Formatting the date on the x-axis
    plt.gca().xaxis.set_major_formatter(DateFormatter('%b %d'))

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel(f'{ticker} Price')
    plt.title(f'Stock Prices for {ticker} (Sep 2023 - Nov 2023)')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Save the plot to a file
    plt.savefig(f'{ticker}.png', bbox_inches='tight')

    # Show the plot
    plt.tight_layout()
    plt.show()
