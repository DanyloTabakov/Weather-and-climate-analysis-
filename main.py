import os
import pandas as pd

from src.download import download_weather_data
from src.preprocessing import (
    load_csv,
    clean_and_sort_temperature_data,
    resample_monthly
)
from src.analisys import (
    add_trend_series,
    calculate_noise,
    summary_statistics
)
from src.plots import (
    plot_temperature,
    plot_with_trend
)

def main():
    # 1. Ensure folders exist
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("results/plots", exist_ok=True)
    os.makedirs("results/summaries", exist_ok=True)

    # 2. Download raw data (if not already present)
    raw_file = "data/raw/warsaw_2010_2020.csv"
    if not os.path.isfile(raw_file):
        download_weather_data(
            latitude=52.23, longitude=21.01,
            start_date="2010-01-01", end_date="2020-12-31",
            filename=raw_file
        )

    # 3. Load & preprocess
    df_raw = load_csv(raw_file)
    df_clean = clean_and_sort_temperature_data(df_raw, date_col='time')
    df_clean.to_csv("data/processed/warsaw_clean.csv", index=False)

    # 4. Resample monthly
    df_monthly = resample_monthly(df_clean, date_col='time')
    df_monthly.to_csv("data/processed/warsaw_monthly.csv", index=False)

    # 5. Analysis on daily data
    df_trended = add_trend_series(df_clean, value_col='temperature_2m_mean')
    noise_std = calculate_noise(df_trended)
    stats = summary_statistics(df_clean, value_col='temperature_2m_mean')

    # 6. Save summary stats
    stats.to_csv("results/summaries/daily_stats.csv")
    print(f"[stats] Daily data noise std: {noise_std:.3f} °C")
    print(stats)

    # 7. Plot and save
    plot_temperature(df_clean,
                     date_col='time',
                     value_col='temperature_2m_mean',
                     save_path="results/plots/daily_temp.png")

    plot_with_trend(df_trended,
                    date_col='time',
                    value_col='temperature_2m_mean',
                    trend_col='trend',
                    save_path="results/plots/daily_temp_trend.png")

    # 8. Plot monthly
    plot_temperature(df_monthly,
                     date_col='time',
                     value_col='monthly_mean',
                     save_path="results/plots/monthly_temp.png")

if __name__ == "__main__":
    main()


