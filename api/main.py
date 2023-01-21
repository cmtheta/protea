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
    # TODO: 他プロバイダのトラフィック画像を取得できるようにする
    # TODO: 他の期間のトラッフィック画像を取得できるようにする
    # TODO: 地域別のトラフィック画像を取得できるようにする
    url = "https://www.jpnap.net/assets/traffic/jpnap_total_day.png"
    return Response(content=fetch_img(url), media_type='image/png')
