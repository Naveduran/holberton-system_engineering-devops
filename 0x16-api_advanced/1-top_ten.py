#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests
import json


def top_ten(subreddit):
    """Return the number of subscribers """
    URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent':
        'AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75'}
    r = requests.get(URL, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print('None')
        return
    children = r.json().get('data').get('children')
    for i in range(0, 10):
        print('{}'.format(children[i].get('data').get('title')))
