# src/visualize.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_avg_temperature(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x=df.index, y='avg_temp_C', hue='decade', marker="o")
    plt.title('Average Yearly Temperature')
    plt.ylabel('Temperature (°C)')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

def plot_total_precipitation(df):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=df, x=df.index, y='total_precip_mm', hue='decade')
    plt.title('Total Yearly Precipitation')
    plt.ylabel('Precipitation (mm)')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

def plot_extreme_days(df):
    fig, ax = plt.subplots(2, 1, figsize=(10, 10))

    sns.lineplot(data=df, x=df.index, y='hot_days_over_30C', hue='decade', marker="o", ax=ax[0])
    ax[0].set_title('Hot Days per Year (>30°C)')
    ax[0].set_ylabel('Number of Days')

    sns.lineplot(data=df, x=df.index, y='freezing_days_below_0C', hue='decade', marker="o", ax=ax[1])
    ax[1].set_title('Freezing Days per Year (<0°C)')
    ax[1].set_ylabel('Number of Days')

    plt.tight_layout()
    plt.show()
