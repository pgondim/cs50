import requests

res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "TLcRX6dv9PVeRxB8tKKo3w", "isbns": "9781632168146"})
data = res.json()
data = data["books"][0]["id"]
print(data)