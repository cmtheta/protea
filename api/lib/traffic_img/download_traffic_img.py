import requests

def fetch_img(img_url):
    # TODO: エラー処理
    r = requests.get(img_url)
    return r.content

if __name__=="__main__":
    url = "https://www.jpnap.net/assets/traffic/jpnap_total_day.png"
