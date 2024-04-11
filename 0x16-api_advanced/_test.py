import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
url = "https://www.reddit.com/subreddits/search.json?q=programming"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)

