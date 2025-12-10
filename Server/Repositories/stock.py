# this file is responsible for the functinality of stock data fetching and returning it

import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime as dt
import heapq
from fastapi import status, HTTPException

# returns a pandas.dataframe containing historical info of a given stock converted to JSON
# from a given start date to a given end date in a given sample (D/W/M/Y)
def getStockData(symbol, startDate, endDate, sample):

   # try fetching data
   try:
      data = web.DataReader(symbol, 'stooq', start=startDate, end=endDate)
   except Exception as e:
    return f'ERROR: {symbol} | {startDate} | {endDate} | {sample}'

   # resample to daily/weekly/monthly/yearly data, taking the last day of each week/month/year
   data = data.resample(sample).last()
   data = data.dropna()
   # for some reason resampling reverse the order of the dataframe, so sort is needed
   data = data.sort_values(by='Date', ascending=False)
   return data.to_json()