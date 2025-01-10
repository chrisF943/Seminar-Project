# Stock Data Collection and Analysis

## Description
This project automates the collection and analysis of daily closing prices for selected stock tickers using Python and cloud-based scheduling. The system fetches data from the AlphaVantage API and generates visualizations to track stock performance over time.

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

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **AlphaVantage API Key**: Obtain a free API key from [AlphaVantage](https://www.alphavantage.co/support/#api-key).
- **Python Libraries**: Install the following packages:
  - `requests`
  - `matplotlib`
  - `schedule`
  - `pandas`

---

## Usage

### Prepare the JSON File
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/chrisF943/Seminar-Project.git
   cd Seminar-Project
   ```

2. **Install Required Packages:**
   ```bash
   pip install requests matplotlib schedule pandas
   ```

3. **Configure the API Key:**
   - Replace `'YOUR_API_KEY'` in `main.py` with your actual AlphaVantage API key.

4. **Run the Script:**
   ```bash
   python main.py
   ```

5. **Automate Execution (Optional):**
   - Deploy the script on a cloud platform like PythonAnywhere.
   - Set up a scheduled task to run `main.py` daily at 6 PM EST on trading days.

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

## Contact
For further questions or feedback, please reach out to the project author via the GitHub repository: [chrisF943/Seminar-Project](https://github.com/chrisF943/Seminar-Project).
