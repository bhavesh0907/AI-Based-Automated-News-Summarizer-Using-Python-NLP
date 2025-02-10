import requests

def fetch_news_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()["articles"]
    return []
