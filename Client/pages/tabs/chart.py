# this file is the 'Chart' tab in the Stock page,
# which shows after getting stock information from the user, and loading its data

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

VOLUME_BAR_COLOR_RGBA = "(128,128,128,0.5)" # grey

# called from the stock page file, this will show the 'Chart' tab widgets
def show(data, sample):

    # resample to daily/weekly/monthly/yearly data, taking the last day of each period
    data = data.resample(sample).last()
    data = data.dropna()

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