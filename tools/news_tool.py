import requests


def get_finance_news(query: str):

    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&apiKey=YOUR_API_KEY"

    response = requests.get(url)

    data = response.json()

    articles = []

    for article in data.get("articles", []):
        articles.append({
            "title": article["title"],
            "source": article["source"]["name"],
            "url": article["url"]
        })

    return articles