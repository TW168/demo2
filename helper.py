import yfinance as yf
import streamlit as st


@st.cache_data
def get_stock_data(tickers, start_date, end_date):
    """
    Fetches historical market data for given ticker symbols between specified dates.

    Parameters:
    tickers (list): A list of string ticker symbols for which to fetch data.
    start_date (str): The start date for the date range in the 'YYYY-MM-DD' format.
    end_date (str): The end date for the date range in the 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: A DataFrame containing the historical market data for the ticker symbols.

    Example usage
    tickers = ['AMZN']  # List of ticker symbols
    start_date = '2013-01-01'  # Start date of the date range
    end_date = '2023-07-14'  # End date of the date range
    stock_data = get_stock_data(tickers, start_date, end_date)
    """
    data = yf.download(tickers, start=start_date, end=end_date, progress=False)

    return data