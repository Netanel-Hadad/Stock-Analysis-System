# stock page implementation
# here we use screen widgets to take input from the user, fetch stock data,
# and show the data in diffrent tabs which are created in different files which can be found in the 'tabs' folder

import streamlit as st
import datetime
import requests
import pandas as pd
import plotly.graph_objects as go
from io import StringIO

# when importing from streamlit files, we are always in the main app file folder,
# meaning we import as if we are in Client folder as this is where the app.py file is
from pages.tabs import general, chart
from pages.tabs import data as dt

SERVER_PATH = "http://localhost:8000" # if we deploy the server in the future, this will have to be changed

# widgets that will stay on the screen no matter what tab the user is in
st.title("Stock information (USD)")
# orginzing the input widgets in 2 columns
col1, col2 = st.columns(2)
with col1:
    symbol = st.text_input("Symbol:", placeholder="")
    startDate = st.date_input("Start Date:", datetime.date(2020, 1, 1), format="YYYY.MM.DD")
with col2:
    sample = st.selectbox("Sample:", ("D", "W", "M", "Y"))
    endDate = st.date_input("End Date:",     datetime.date.today(), format="YYYY.MM.DD")

# load stock information button
if st.button('Load stock information'):
    # get the stock info as a json string from the server
    url = f"{SERVER_PATH}/stock/{symbol}"
    headers = {'Content-Type': 'application/json'}
    params = {"startDate": startDate, "endDate": endDate}
    response = requests.get(url, headers=headers, params=params)
    # convert json string to json
    dataJson = response.json()
    # convert json to dataframe
    # we use StringIO because not doing so will cause a warning saying that "Passing literal json to 'read_json' 
    # is deprecated and will be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object"
    data = pd.read_json(StringIO(dataJson))

    # after loading the stock data, we create diffrent tabs
    generalTab, chartTab, dataTab = st.tabs(["General", "Chart", "Data"])

    # creat tabs from the matching file which can be found in the 'tabs' folder
    with generalTab:
        general.show(data)
    with chartTab:
        chart.show(data, sample)
    with dataTab:
        dt.show(data)