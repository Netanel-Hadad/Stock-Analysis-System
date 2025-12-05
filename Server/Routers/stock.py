# this is the router for handling requests related to reports (only handling requests)
# the funcions that are responsible for doing what the user wanted are in the Repository folder

from fastapi import APIRouter, Depends, status, Response
from ..Repositories import stock as st

router = APIRouter(
    prefix="/stock", # the start of the path
    tags=['stocks'] # tags in which the path function will be in the debugger (path/docs)
)

# get stock data as json
@router.get('/{symbol}')
def getStockData(symbol:str, startDate:str, endDate:str, sample:str):
    return st.getStockData(symbol, startDate, endDate, sample)