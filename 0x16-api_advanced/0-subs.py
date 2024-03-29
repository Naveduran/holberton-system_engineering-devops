#!/usr/bin/python3
""" Returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers """
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent':
        'AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75'}
    r = requests.get(URL, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return (0)
    subs = r.json().get('data').get('subscribers')
    return (subs)
