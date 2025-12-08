# this is the streamlit application for viewing the stock data

import streamlit as st
import datetime
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from io import StringIO

PATH = "http://localhost:8000"
VOLUME_BAR_COLOR_RGBA = "(128,128,128,0.5)"

# user screen objects
st.title("Stock Analysis Syetem")
# input objects
symbol = st.text_input("Symbol:", placeholder="GOOG")
startDate = st.date_input("Start Date:", datetime.date(2024, 1, 1), format="YYYY.MM.DD")
endDate = st.date_input("End Date:",     datetime.date.today(), format="YYYY.MM.DD")
sample = st.selectbox("Sample:", ("D", "W", "M", "Y"))

# view candle stick chart button
if st.button('View'):
    # get the stock info as a json string
    url = f"{PATH}/stock/{symbol}"
    headers = {'Content-Type': 'application/json'}
    params = {"startDate": startDate, "endDate": endDate, "sample": sample}
    response = requests.get(url, headers=headers, params=params)
    # convert json string to json
    dataJson = response.json()
    # convert json to dataframe
    # we use StringIO because not doing so will cause a warning saying that 'Passing literal json to 'read_json' 
    # is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object'
    data = pd.read_json(StringIO(dataJson))

    # creating the charts
    candleSticks = go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name="Candlesticks")
    volumeBars = go.Bar(
                x=data.index,
                y=data['Volume'],
                showlegend=True,
                name="Volume",
                marker={
                    "color":f"rgba{VOLUME_BAR_COLOR_RGBA}"
                },
                # setting the base range of volume values to 0 and the max value in the Volume column times 6
                # seems like a good amount for the best chart readability
                base=[0, data['Volume'].max()*6]
    )

    # combining all the charts into one figure
    fig = go.Figure(candleSticks)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(candleSticks, secondary_y=True)
    fig.add_trace(volumeBars, secondary_y=False)
    fig.update_layout(
        title="",
        height=500,
        # hide Plotly scrolling minimap below the price chart
        xaxis={"rangeslider": {"visible": False}},
    )
    fig.update_yaxes(title="Price", secondary_y=True, showgrid=True)
    fig.update_yaxes(title="Volume", secondary_y=False, showgrid=False)
    
    st.plotly_chart(fig)