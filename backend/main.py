from fastapi import FastAPI

from .seed import seed_values
from .converter import convert

app = FastAPI()


@app.get('/')
def index():
    return {"Hello": "From GuysPortfolio :)"}


@app.get('/api')
def api():
    portfolio = {}
    for date, value in seed_values.items():
        portfolio[date] = convert(value)
    return {"data": portfolio}
