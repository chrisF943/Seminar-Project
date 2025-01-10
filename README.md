# Collecting and Analyzing Stock Data with Python

## Overview
Created for the Seminar in Advanced Software Development course, this project automates the collection and analysis of daily closing prices for selected stock tickers using Python and cloud-based scheduling. The system fetches data from the AlphaVantage API and generates visualizations to track stock performance over time.

---

## Features
1. **Automated Data Collection:**
   - Utilizes the AlphaVantage API to retrieve daily closing prices for specified stock tickers.
   - Deployed on PythonAnywhere to execute automatically at 6 PM EST on trading days.

2. **Data Analysis and Visualization:**
   - Processes the collected data to generate graphs illustrating stock performance.
   - Supports multiple stock tickers, including AAPL, AMZN, GOOGL, and MSFT.

3. **Historical Data Management:**
   - Stores historical data in text files for reference and further analysis.
   - Generates visual comparisons of stock performance over different time periods.

---

## Key Functions

### Data Collection (`main.py`):
- Fetches daily closing prices for specified stock tickers using the AlphaVantage API.
- Appends new data to existing historical records.

### Data Visualization (`2024_graphs.py`):
- Generates line graphs for each stock ticker to visualize performance over time.
- Saves the graphs as PNG images for review and reporting.

### Historical Data Management (`file_gen.py`):
- Creates and updates text files containing historical stock data.
- Ensures data integrity and readiness for analysis.

---

## Performance Highlights
- **Automation:** Eliminates manual data collection by automating daily retrieval and storage.
- **Visualization:** Provides clear graphical representations of stock trends over time.
- **Scalability:** Easily extendable to include additional stock tickers or different data points.

---

## Video Presentation

[Project Presentation](https://youtu.be/jG8ikQyUJII)

---

All materials used in presentation are available in this repository.
