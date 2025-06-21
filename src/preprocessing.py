import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(filepath)

def clean_and_sort_temperature_data(df: pd.DataFrame,
                                    date_col: str = 'time') -> pd.DataFrame:
    """
    Convert `date_col` to datetime, drop rows with missing dates,
    sort by date, reset index.
    """
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna(subset=[date_col])
    df = df.sort_values(by=date_col).reset_index(drop=True)
    return df

def resample_monthly(df: pd.DataFrame,
                     date_col: str = 'time',
                     value_col: str = 'temperature_2m_mean') -> pd.DataFrame:
    """
    Resample daily data to monthly means.
    """
    df = df.set_index(date_col)
    monthly = df[value_col].resample('M').mean().to_frame()
    monthly = monthly.reset_index()
    monthly.rename(columns={value_col: 'monthly_mean'}, inplace=True)
    return monthly
