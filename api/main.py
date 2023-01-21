from fastapi import FastAPI
from lib.greeting import Greeting

app = FastAPI()

@app.get("/")
def index():
    return {"hello" : "world"}

@app.get("/hello")
def hello(name: str):
    return {"message": Greeting.hello_with_name(name)}
