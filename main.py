# main.py

from datetime import datetime
from src.fetch_data import fetch_decade_data
from src.process_data import summarize_yearly
from src.visualize import (
    plot_avg_temperature,
    plot_total_precipitation,
    plot_extreme_days
)
import pandas as pd

# --- 1. Set location: Central Park, NYC ---
latitude = 40.7829
longitude = -73.9654

# --- 2. Define periods ---
decades = {
    '1980s': (1980, 1989),
    '2010s': (2010, 2020)
}

# --- 3. Fetch and process data ---
summaries = []

for label, (start_year, end_year) in decades.items():
    print(f"Fetching data for {label}...")
    daily_data = fetch_decade_data(latitude, longitude, start_year, end_year)
    summary = summarize_yearly(daily_data, label)
    summaries.append(summary)

# --- 4. Combine into one DataFrame ---
combined = pd.concat(summaries)
print("\nCombined yearly summary:")
print(combined)

# --- 5. Generate plots ---
plot_avg_temperature(combined)
plot_total_precipitation(combined)
plot_extreme_days(combined)
