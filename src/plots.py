# here wiil be plotting functions
import matplotlib.pyplot as plt
import os

def plot_temperature(df,
                     date_col: str = 'time',
                     value_col: str = 'temperature_2m_mean',
                     save_path: str = None):
    plt.figure(figsize=(12, 4))
    plt.plot(df[date_col], df[value_col], label='Mean Temp')
    plt.title("Daily Mean Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
        print(f"[plot] Saved to {save_path}")
    else:
        plt.show()
    plt.close()

def plot_with_trend(df,
                    date_col: str = 'time',
                    value_col: str = 'temperature_2m_mean',
                    trend_col: str = 'trend',
                    save_path: str = None):
    plt.figure(figsize=(12, 4))
    plt.plot(df[date_col], df[value_col], label='Actual')
    plt.plot(df[date_col], df[trend_col], '--', label='Trend')
    plt.title("Temperature with Trend Line")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
        print(f"[plot] Saved to {save_path}")
    else:
        plt.show()
    plt.close()