#!/usr/bin/python3
"""Reddit API"""


def number_of_subscribers(subreddit):
    """Returns the number of subscribers in a subreddit"""
    import requests

    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 300:
        return 0
    else:
        [print(post.get["data"]["title"])
            for post in res.json()["data"]["children"]]
