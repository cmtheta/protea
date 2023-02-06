import requests

def fetch_img(provider: str, range: str, area: str):
    # TODO: 他プロバイダのトラフィック画像を取得できるようにする
    # TODO: 他の期間のトラッフィック画像を取得できるようにする
    # TODO: 地域別のトラフィック画像を取得できるようにする
    img_url = "https://www.jpnap.net/assets/traffic/jpnap_total_day.png"

    # TODO: エラー処理
    r = requests.get(img_url)
    return r.content
