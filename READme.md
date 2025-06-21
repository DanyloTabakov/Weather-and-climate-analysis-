# 🌦️ Weather and Climate Data Analysis

This project analyzes historical weather data (specifically temperature) to explore **long-term trends**, **short-term noise**, and **basic statistics**. Data is downloaded automatically via the Open-Meteo API, cleaned, processed, analyzed, and visualized in a reproducible Python pipeline.

---

## 🚀 How to Run

### 1. 📦 Install Requirements
You need Python 3.8+.

```bash
pip install -r requirements.txt
python main.py

This will:
    - Download historical daily temperature data (2010–2020) for Warsaw, Poland
    - Clean and sort it
    - Calculate monthly averages
    - Add a linear trend line
    - Measure noise (short-term fluctuations)
    - Generate plots and save summary statistics


## 📁 Project Structure
weather_project/
├── src/ # Modular code
│ ├── download.py # API download functions
│ ├── preprocessing.py # Data cleaning and resampling
│ ├── analysis.py # Trend, noise, and stats computation
│ └── visualization.py # Plotting functions
├── data/
│ ├── raw/ # Raw CSVs from the API
│ └── processed/ # Cleaned & resampled data
├── results/
│ ├── plots/ # PNG plots of temperature trends
│ └── summaries/ # Summary statistics CSV
├── main.py # Main script to run everything
├── requirements.txt # All needed Python libraries
└── .gitignore # Ignore data/ and results/ folders


📊 Output

Plots:
Saved in results/plots/
→ Daily temperature, daily with trend, monthly averages
Statistics:
Saved in results/summaries/daily_stats.csv
→ Count, mean, std, min, quartiles, max


🧠 Key Concepts

Trend = long-term direction in the data (e.g. warming)
Noise = short-term random variation (e.g. weather chaos)
Statistics = mean, standard deviation, etc.


🌐 Data Source

Data is downloaded from Open-Meteo Historical API.


🛠️ Dependencies

pandas
numpy
matplotlib
scipy
requests


📌 Example Use

Want to change the city or date range?
Just edit the values inside main.py:

download_weather_data(
    latitude=YOUR_LAT,
    longitude=YOUR_LON,
    start_date="YYYY-MM-DD",
    end_date="YYYY-MM-DD",
    filename="data/raw/your_file.csv"
)
