# this file is the 'General' tab in the Stock page,
# which shows after getting stock information from the user, and loading its data
# this file does all the calulcations needed for showing the request data

import streamlit as st
import numpy
import pandas as pd
from pandas.tseries.offsets import DateOffset

# called from the stock page file, this will show the 'Data' tab widgets
def show(data): 
    # the make the data look cleaner and more readable,
    # we seperate the text and the values into diffrent columns
    # to make the text and the values in the same line, make sure that the st.write commands
    # for the text and the values in the diffrent columns are in the same order
    textCol, valuesCol = st.columns(2)
    with textCol:
        st.write("Prev. Close:")
        st.write("Day's Range:")
        st.write("52 Weeks Range:")
        st.write("1 Year ROI:")
    with valuesCol:
        st.write(str(data.head(1).Close.values[0]))
        st.write(str(data.head(1).Low.values[0]) + " - " + str(data.head(1).High.values[0]))
        st.write(get52WeeksRange(data))
        st.write(str(getROI(data)) + "%")

# calculate stock current ROI
def getROI(data):
    costOfInvesment = data.shift(-365)['Close'].values[0]
    netProfit = data['Close'].values[0] - costOfInvesment
    ROI = 100 * netProfit / costOfInvesment 
    # round the value and return it with only 2 digits after the dot
    return round(ROI, 2)

# calulate and return a string of the last 52 weeks price range
def get52WeeksRange(data):
    # we want to get the most accurate data,
    # and for that we want to get the data of the prices that were at most 365 days ago
    # so we will get the range exactly 365 days backwards and not for example take 'only' 252 trading days
    # which might not be the most accurate data
    lastDate = data.index.max()
    startDate = lastDate - DateOffset(weeks=52)
    # mask for filtering the data
    mask = (data.index > startDate) & (data.index <= lastDate)
    # creating the dataframse of only the relevant data
    lastYearData = data.loc[mask]
    high = lastYearData['High'].max()
    low = lastYearData['Low'].min()
    return f"{low} - {high}"