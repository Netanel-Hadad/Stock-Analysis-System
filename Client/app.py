# this is the streamlit main application file
# from here we start the application and create the navigation side-bar in order to switch pages

import streamlit as st

# defining all pages in the application
homePage = st.Page("pages/home.py", title="Home")
stockPage = st.Page("pages/stock.py", title="Stock")
screenerPage = st.Page("pages/screener.py", title="Screener")

# defining and running the navigation side-bar with all its contents
pg = st.navigation([homePage, stockPage, screenerPage])
pg.run()