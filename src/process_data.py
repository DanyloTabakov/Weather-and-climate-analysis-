# src/process_data.py

import pandas as pd

def summarize_yearly(df, label):
    """
    Aggregates daily weather data into yearly statistics:
    - Average temperature
    - Total precipitation
    - Number of hot days (>30°C)
    - Number of freezing days (<0°C)
    Adds a 'decade' label column.
    """
    df = df.dropna(subset=['tavg', 'prcp', 'tmax', 'tmin'])
    df['year'] = df.index.year

    summary = df.groupby('year').agg({
        'tavg': 'mean',
        'prcp': 'sum',
        'tmax': lambda x: (x > 30).sum(),
        'tmin': lambda x: (x < 0).sum()
    })

    summary.columns = ['avg_temp_C', 'total_precip_mm', 'hot_days_over_30C', 'freezing_days_below_0C']
    summary['decade'] = label

    return summary
