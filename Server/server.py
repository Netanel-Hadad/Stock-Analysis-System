# this is the server file which is the backend of the platform 
# all of the requests by the users are handles by routers

from fastapi import FastAPI
from .Routers import stock

app = FastAPI()

# routers
app.include_router(stock.router)