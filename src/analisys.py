import numpy as np
import pandas as pd
from scipy.stats import linregress

def compute_trend(df: pd.DataFrame,
                  value_col: str = 'temperature_2m_mean') -> tuple:
    """
    Perform linear regression against time index to get slope & intercept.
    Returns (slope, intercept).
    """
    x = np.arange(len(df))
    y = df[value_col].values
    slope, intercept, _, _, _ = linregress(x, y)
    return slope, intercept

def add_trend_series(df: pd.DataFrame,
                     value_col: str = 'temperature_2m_mean',
                     trend_col: str = 'trend') -> pd.DataFrame:
    """
    Add a trend line column to df based on linear regression.
    """
    slope, intercept = compute_trend(df, value_col)
    df[trend_col] = intercept + slope * np.arange(len(df))
    return df

def calculate_noise(df: pd.DataFrame,
                    value_col: str = 'temperature_2m_mean',
                    trend_col: str = 'trend',
                    residual_col: str = 'residual') -> float:
    """
    Compute the residuals (value minus trend) and return their standard deviation.
    """
    df[residual_col] = df[value_col] - df[trend_col]
    noise_std = df[residual_col].std()
    return noise_std

def summary_statistics(df: pd.DataFrame,
                       value_col: str = 'temperature_2m_mean') -> pd.Series:
    """
    Return a pandas Series with count, mean, std, min, quartiles, and max.
    """
    return df[value_col].describe()