import pandas as pd
import requests

def download_weather_data(latitude: float,
                          longitude: float,
                          start_date: str,
                          end_date: str,
                          filename: str) -> pd.DataFrame:
    """
    Download daily temperature data from Open-Meteo for a given period and location,
    save to CSV at `filename`, and return as DataFrame.
    """
    url = (
        "https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date={start_date}&end_date={end_date}"
        "&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean"
        "&timezone=auto"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json().get('daily', {})
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"[download] Saved raw data to {filename}")
    return df

