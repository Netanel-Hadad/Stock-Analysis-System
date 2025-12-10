# this file is the 'General' tab in the Stock page,
# which shows after getting stock information from the user, and loading its data

import streamlit as st

# called from the stock page file, this will show the 'Data' tab widgets
def show(data):
    st.write("GENERAL TAB")