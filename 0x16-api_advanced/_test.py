import requests
from sys import argv

subreddit = argv[1]
url = f'https://www.reddit.com/r/{subreddit}/about.json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convert the response to JSON format
    # Now you can work with the data returned by the API
    print(data)
else:
    print('Failed to retrieve data from API. Status code:', response.status_code)
