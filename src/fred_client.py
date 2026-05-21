# src/fred_client.py

from fredapi import Fred
import pandas as pd


def create_fred_client(api_key):
    """
    Create and return a Fred API client.
    """

    fred = Fred(api_key=api_key)

    return fred


def fetch_series(fred, series_id):
    """
    Fetch a single FRED series and return it as a clean DataFrame.

    Parameters:
        fred: Fred API client
        series_id: FRED series code (example: 'UNRATE')

    Returns:
        pandas DataFrame with:
        - date
        - value
    """

    series = fred.get_series(series_id)

    df = series.reset_index()

    df.columns = ["date", "value"]

    return df


def fetch_named_series(fred, series_id, column_name):
    """
    Fetch a FRED series and rename the value column.

    Example:
        fetch_named_series(fred, "UNRATE", "unemployment_rate")
    """

    df = fetch_series(fred, series_id)

    df = df.rename(columns={"value": column_name})

    return df


def get_unemployment_data(api_key):
    """
    Convenience function specifically for unemployment data.
    """

    fred = create_fred_client(api_key)

    df = fetch_named_series(
        fred,
        "UNRATE",
        "unemployment_rate"
    )

    return df


def get_cpi_data(api_key):
    """
    Fetch CPI inflation data.
    """

    fred = create_fred_client(api_key)

    df = fetch_named_series(
        fred,
        "CPIAUCSL",
        "cpi"
    )

    return df


def get_fed_funds_rate(api_key):
    """
    Fetch Federal Funds Rate data.
    """

    fred = create_fred_client(api_key)

    df = fetch_named_series(
        fred,
        "FEDFUNDS",
        "fed_funds_rate"
    )

    return df