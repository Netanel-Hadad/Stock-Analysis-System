# this is the server main entry file
# all of the requests by the users are handles using routers
# which can be found in the Routers folder

from fastapi import FastAPI
from .Routers import stock

app = FastAPI()

# routers
app.include_router(stock.router)