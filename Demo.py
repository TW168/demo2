import streamlit as st
import pandas as pd
import numpy as np
import pandas_ta as ta
from helper import get_stock_data
import plotly.graph_objects as go
from plotly.subplots import make_subplots


st.set_page_config(
    page_title="Demo 1", layout="wide", menu_items={"About": "tony.wei@outlook.com"}
)

st.title("Demo 1")


tickers = 'GOOG'  # List of ticker symbols
start_date = '2013-01-01'  # Start date of the date range
end_date = '2023-07-25'  # End date of the date range
stock_data = get_stock_data(tickers=tickers, start_date=start_date, end_date=end_date)

# Calculate the EMA with a length of 10 periods
stock_data['EMA_10'] = ta.ema(stock_data['Close'], length=10)

# Calculate the RSI with a length of 14 periods
stock_data['RSI'] = ta.rsi(stock_data['Close'], length=14)

# Calculate the MACD with short length=12, long length=26 and signal length=9
stock_data['MACD'] = ta.macd(stock_data['Close'], fast=12, slow=26, signal=9)['MACD_12_26_9']


with st.expander("Graphs", expanded=False):
    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=3, cols=1)

    # Add traces
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name='Close'), row=1, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], name='RSI'), row=2, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MACD'], name='MACD'), row=3, col=1)

    # Update xaxis properties
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_xaxes(title_text="Date", row=3, col=1)

    # Update yaxis properties
    fig.update_yaxes(title_text="Close Price", row=1, col=1)
    fig.update_yaxes(title_text="RSI", row=2, col=1)
    fig.update_yaxes(title_text="MACD", row=3, col=1)

    # Update title and height
    fig.update_layout(title_text=f"{tickers} Stock Price with RSI and MACD", height=700)

    st.plotly_chart(fig)

    # Create figure and plot 'Close' prices and Volume
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], name='Stock Price'))

    # Add 'Volume' as a bar chart trace
    fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'], name='Volume', yaxis='y2', marker=dict(color='green', opacity=0.1)))

    # Update layout and axis labels
    fig.update_layout(
        title= f'{tickers} Stock Price and Volume',
        yaxis=dict(title='Stock Price'),
        yaxis2=dict(title='Volume', overlaying='y', side='right'),
        xaxis=dict(title='Date'),
    )

    # Set up two separate legends
    fig.update_layout(
        legend=dict(
            traceorder='normal',
            font=dict(size=10),
            yanchor='top',
            y=0.99,
            xanchor='left',
            x=0.01
        ),
        annotations=[
            dict(
                text="Stock Price",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.01,
                y=1.01,
                xanchor='left',
                yanchor='bottom',
                font=dict(size=10),
            ),
            dict(
                text="Volume",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.99,
                y=1.01,
                xanchor='right',
                yanchor='bottom',
                font=dict(size=10),
            )
        ]
    )

    # Show the plot
    st.plotly_chart(fig)

# Calculate Bollinger Bands
stock_data.ta.bbands(close='Close', length=20, std=2, append=True)
st.dataframe(stock_data)


# Create a Plotly figure
fig = go.Figure()

# Add traces for close price, upper band, middle band, and lower band
# Add Candlestick trace
fig.add_trace(go.Candlestick(
    x=stock_data.index, 
    open=stock_data['Open'], 
    high=stock_data['High'], 
    low=stock_data['Low'], 
    close=stock_data['Close'], 
    name='Candlestick'))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BBU_20_2.0'], mode='lines', name='Upper Band', line=dict(color='rgba(255, 165, 0, 0.4)')))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BBM_20_2.0'], mode='lines', name='Middle Band', line=dict(color='rgba(75, 0, 130, 0.4)')))
fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['BBL_20_2.0'], mode='lines', name='Lower Band', line=dict(color='rgba(0, 0, 255, 0.4)')))

# Set figure layout
fig.update_layout(title=f'{tickers} Bollinger Bands', xaxis_title='Date', yaxis_title='Price', width=1500, height=1000,)

# Show the figure
st.plotly_chart(fig)