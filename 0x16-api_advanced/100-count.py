#!/usr/bin/python3
"""count words in titles"""
import requests


def to_text(hot_dict):
    """printing function """
    if len(hot_dict) == 0:
        return ''
    text = ''
    ordered_by_alpha = sorted(hot_dict.items(),
                              key=lambda tup: tup[0],
                              reverse=False)
    ordered_by_values = sorted(ordered_by_alpha,
                               key=lambda tup: tup[1],
                               reverse=True)
    for key in ordered_by_values:
        value = hot_dict.get(key[0])
        text += key[0] + ': ' + str(value) + '\n'
    print(text, end='')


def count_words(subreddit, word_list, after='', hot_dict={}):
    """Parse the titles of subreddit posts to return a sorted count
    of given keywords """

    # Request titles one by one (using after and a limit)
    # using a custom user agent to avoid errors about 'too many requests'

    url = 'https://www.reddit.com/r/{}/hot.json?after={}&limit=1'.format(
        subreddit, after)

    headers = {
        'User-Agent':
        'Nat'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    # If the resquest fail, do not run the rest of the code
    if r.status_code != 200:
        return

    # Get the data from the json
    data = r.json().get('data')

    # If there are no more elements to check --> print!
    if len(data.get('children')) == 0:
        return to_text(hot_dict)

    # Get the tittle of this post and turn to lower case,
    title = data.get('children')[0].get('data').get('title').lower()

    # Split words of the title, put in a list to search easier
    title_words = title.split()

    # If a desired word is in the title --> Add count to the dictionary
    for word in word_list:
        if title_words.count(word):
            if word in hot_dict:
                number = hot_dict.get(word) + title_words.count(word)
                hot_dict.update({word: number})
            else:
                hot_dict.update({word: title_words.count(word)})

    # Call this recursive function for the next reddit post
    after = data.get('after')
    count_words(subreddit, word_list, after, hot_dict)
