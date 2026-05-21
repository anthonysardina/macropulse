# src/indicators.py

import pandas as pd


def calculate_pct_change(df, column_name, periods=12):
    """
    Calculate percent change over a specified number of periods.

    Example:
        Monthly CPI data with periods=12
        gives year-over-year inflation.

    Parameters:
        df : pandas DataFrame
        column_name : column to calculate percent change on
        periods : number of periods to compare against

    Returns:
        DataFrame with new percent change column
    """

    df = df.copy()

    new_column_name = f"{column_name}_pct_change"

    df[new_column_name] = (
        df[column_name].pct_change(periods=periods) * 100
    )

    return df


def calculate_difference(df, column_name):
    """
    Calculate simple period-to-period difference.

    Example:
        unemployment_rate difference from previous month.

    Returns:
        DataFrame with difference column.
    """

    df = df.copy()

    new_column_name = f"{column_name}_diff"

    df[new_column_name] = df[column_name].diff()

    return df


def calculate_moving_average(df, column_name, window=12):
    """
    Calculate moving average.

    Parameters:
        window : rolling window size

    Returns:
        DataFrame with moving average column
    """

    df = df.copy()

    new_column_name = f"{column_name}_ma_{window}"

    df[new_column_name] = (
        df[column_name]
        .rolling(window=window)
        .mean()
    )

    return df


def calculate_rolling_std(df, column_name, window=12):
    """
    Calculate rolling standard deviation.

    Useful for measuring volatility.
    """

    df = df.copy()

    new_column_name = f"{column_name}_std_{window}"

    df[new_column_name] = (
        df[column_name]
        .rolling(window=window)
        .std()
    )

    return df


def standardize_column(df, column_name):
    """
    Standardize a column using z-score normalization.

    Formula:
        (value - mean) / standard deviation
    """

    df = df.copy()

    mean = df[column_name].mean()

    std = df[column_name].std()

    new_column_name = f"{column_name}_zscore"

    df[new_column_name] = (
        (df[column_name] - mean) / std
    )

    return df


def create_threshold_flag(
    df,
    column_name,
    threshold,
    flag_name,
    greater_than=True
):
    """
    Create a boolean warning/signal column.

    Examples:
        unemployment above 6%
        inflation above 4%
    """

    df = df.copy()

    if greater_than:
        df[flag_name] = df[column_name] >= threshold
    else:
        df[flag_name] = df[column_name] <= threshold

    return df


def add_recession_flag(df, threshold=6.0):
    """
    Simple unemployment-based recession warning.

    NOT an official recession indicator.
    """

    df = df.copy()

    df["recession_warning"] = (
        df["unemployment_rate"] >= threshold
    )

    return df


def merge_indicator_dataframes(dataframes, on="date"):
    """
    Merge multiple indicator DataFrames together.

    Parameters:
        dataframes : list of DataFrames
        on : merge column

    Returns:
        Combined DataFrame
    """

    if len(dataframes) == 0:
        return pd.DataFrame()

    merged_df = dataframes[0]

    for df in dataframes[1:]:

        merged_df = pd.merge(
            merged_df,
            df,
            on=on,
            how="inner"
        )

    return merged_df


def filter_date_range(df, start_date=None, end_date=None):
    """
    Filter DataFrame by date range.
    """

    df = df.copy()

    if start_date is not None:
        df = df[df["date"] >= start_date]

    if end_date is not None:
        df = df[df["date"] <= end_date]

    return df


def add_year_column(df):
    """
    Add a year column extracted from date.
    """

    df = df.copy()

    df["year"] = pd.to_datetime(df["date"]).dt.year

    return df


def add_month_column(df):
    """
    Add month column extracted from date.
    """

    df = df.copy()

    df["month"] = pd.to_datetime(df["date"]).dt.month

    return df


def remove_missing_values(df):
    """
    Remove rows containing missing values.
    """

    df = df.copy()

    df = df.dropna()

    return df


def rename_value_column(df, new_name):
    """
    Rename generic 'value' column.
    """

    df = df.copy()

    df = df.rename(
        columns={"value": new_name}
    )

    return df


def calculate_correlation(df, column_1, column_2):
    """
    Calculate correlation between two columns.
    """

    correlation = df[column_1].corr(df[column_2])

    return correlation


def summarize_indicator(df, column_name):
    """
    Return simple summary statistics.
    """

    summary = {
        "mean": df[column_name].mean(),
        "median": df[column_name].median(),
        "min": df[column_name].min(),
        "max": df[column_name].max(),
        "std": df[column_name].std()
    }

    return summary