from fastapi import FastAPI, Response
from lib.greeting import Greeting
from lib.traffic_img import fetch_img

app = FastAPI()

@app.get("/")
def index():
    return {"hello" : "world"}

@app.get("/hello")
def hello(name: str):
    return {"message": Greeting.hello_with_name(name)}

@app.get("/traffic_img")
def traffic_img(provider: str, range: str, area: str):
    return Response(content=fetch_img(provider, range, area), media_type='image/png')
