#!/usr/bin/python3
"""count words in titles"""
import requests


def to_text(hot_dict):
    """printing function """
    if len(hot_dict) == 0:
        return ''
    text = ''
    keys = sorted(hot_dict.items(), key=lambda tup: tup[1], reverse=True)
    for key in keys:
        value = hot_dict.get(key[0])
        text += key[0] + ': ' + str(value) + '\n'
    print(text, end='')


def count_words(subreddit, word_list, after='', hot_dict={}):
    """Return a sorted count of given keywords """

    # URL request with an after and a limit
    URL = 'https://www.reddit.com/r/{}/hot.json?after={}&limit=1'.format(
        subreddit, after)
    headers = {
        'User-Agent':
        'Nat'}
    r = requests.get(URL, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    # Check the data
    data = r.json().get('data')

    if len(data.get('children')) == 0:
        return to_text(hot_dict)

    # Get the tittle and parse it
    title = data.get('children')[0].get('data').get('title')
    for word in word_list:
        if title.count(word):
            if word in hot_dict:
                number = hot_dict.get(word) + title.count(word)
                hot_dict.update({word: number})
            else:
                hot_dict.update({word: 1})

    # Make a new recursive call
    after = data.get('after')
    count_words(subreddit, word_list, after, hot_dict)
