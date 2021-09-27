#!/usr/bin/python3
"""creates a list with all the titles of reddit post"""
import requests
import json
import copy


def recurse(subreddit, hot_list=[], after=''):
    """Return a list of titles """

    # URL request with an after and a limit
    URL = 'https://www.reddit.com/r/{}/hot.json?after={}&limit=1'.format(
        subreddit, after)
    headers = {
        'User-Agent':
        'AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75'}
    r = requests.get(URL, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return (None)

    # Check the data
    data = r.json().get('data')

    if len(data.get('children')) == 0:
        return (hot_list)

    # Get the tittle and append it
    child_title = data.get('children')[0].get('data').get('title')
    hot_list.append(child_title)

    # Make a new recursive call
    after = data.get('after')
    hot_list = recurse(subreddit, hot_list, after)
    return hot_list
