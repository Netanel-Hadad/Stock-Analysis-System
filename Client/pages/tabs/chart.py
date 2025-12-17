# this file is the 'Chart' tab in the Stock page,
# which shows after getting stock information from the user, and loading its data

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

INCREASING_CANDLETICK_COLOR = 'green'
DECREASING_CANDLESTICK_COLOR = 'red'
INCREASING_VOLUME_BAR_COLOR_RGBA = "(0,175,0,0.5)"
DECREASING_VOLUME_BAR_COLOR_RGBA = "(175,0,0,0.5)"
PRICE_AVERAGE_WINDOW_SIZE = 100
PRICE_AVERAGE_LINE_COLOR = 'red'
VOLUME_AVERAGE_WINDOW_SIZE = 100
VOLUME_AVERAGE_LINE_COLOR = 'red'

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
                name="Candlesticks",
                increasing_line_color=INCREASING_CANDLETICK_COLOR,
                decreasing_line_color=DECREASING_CANDLESTICK_COLOR)
    
    # we sperate the volumes bars into increasing and decreasing bars like the candlestick chart
    # we sperate them using a mask
    volumeMask = data['Volume'] > data['Volume'].shift(1)
    greenVolumeBarsData = data[volumeMask]
    volumeMask = data['Volume'] <= data['Volume'].shift(1)
    redVolumeBarsData = data[volumeMask]

    # creating the two volume bars
    greenVolumeBars = go.Bar(
                x=greenVolumeBarsData.index,
                y=greenVolumeBarsData['Volume'],
                showlegend=False,
                name="Volume",
                marker={
                    "color":f"rgba{INCREASING_VOLUME_BAR_COLOR_RGBA}"
                },
                # setting the base range of volume values to 0 and the max value in the Volume column times 6
                # seems like a good amount for the best chart readability
                base=[0, data['Volume'].max()*6]
    )
    redVolumeBars = go.Bar(
                x=redVolumeBarsData.index,
                y=redVolumeBarsData['Volume'],
                showlegend=False,
                name="Volume",
                marker={
                    "color":f"rgba{DECREASING_VOLUME_BAR_COLOR_RGBA}"
                },
                # setting the base range of volume values to 0 and the max value in the Volume column times 6
                # seems like a good amount for the best chart readability
                base=[0, data['Volume'].max()*6]
    )

    # creating an average close price line using pandas rolling
    # the average is of the (PRICE_AVERAGE_WINDOW_SIZE) last days
    # notice that we start getting values after (PRICE_AVERAGE_WINDOW_SIZE) days
    # we can set min_periods=1 in the rolling function parameters to change that
    priceAverage = data['Close'].rolling(window = PRICE_AVERAGE_WINDOW_SIZE).mean()
    priceAverageLine = go.Scatter(
        x=priceAverage.index,
        y=priceAverage,
        mode='lines',
        showlegend=True,
        name=f"{PRICE_AVERAGE_WINDOW_SIZE} Day Average Close Price",
        line=dict(color=PRICE_AVERAGE_LINE_COLOR, width=1)
    )

    # creating an average volume line similar to the way we did the average close price line
    volumeAverage = data['Volume'].rolling(window = VOLUME_AVERAGE_WINDOW_SIZE).mean()
    volumeAverageLine = go.Scatter(
        x=volumeAverage.index,
        y=volumeAverage,
        mode='lines',
        showlegend=True,
        name=f"{PRICE_AVERAGE_WINDOW_SIZE} Day Average Volume",
        line=dict(color=VOLUME_AVERAGE_LINE_COLOR, width=0.5)
    )

    # combining all the charts into one figure
    # create the figure and a secondary y
    fig = go.Figure(candleSticks)
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # add all the graphs into the figure
    fig.add_trace(candleSticks, secondary_y=True)
    fig.add_trace(greenVolumeBars, secondary_y=False)
    fig.add_trace(redVolumeBars, secondary_y=False)
    fig.add_trace(priceAverageLine, secondary_y=True)
    fig.add_trace(volumeAverageLine, secondary_y=False)

    # editing figure layout
    fig.update_layout(
        title="",
        height=500,
        # hide Plotly scrolling minimap below the price chart
        xaxis={"rangeslider": {"visible": False}},
    )
    fig.update_yaxes(title="Price", secondary_y=True, showgrid=True)
    fig.update_yaxes(title="Volume", secondary_y=False, showgrid=False)
    
    st.plotly_chart(fig)