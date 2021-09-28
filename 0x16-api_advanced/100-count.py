#!/usr/bin/python3
"""count words in titles"""
import requests


def to_text(hot_dict):
    """ Input: A dictionary.
    Sort keys alphabetically and values in descending order.
    Then, print the dictionary"""
    text = ''
    if len(hot_dict) == 0:
        return text
    ordered_by_alpha = sorted(hot_dict.items(),
                              key=lambda tup: tup[0],
                              reverse=False)
    ordered_by_values = sorted(ordered_by_alpha,
                               key=lambda tup: tup[1],
                               reverse=True)
    for key in ordered_by_values:
        value = hot_dict[key[0]]
        text += key[0] + ': ' + str(value) + '\n'
    print(text, end='')


def count_words(subreddit, word_list, after='', hot_dict={}):
    """Parse the titles of subreddit posts to return a sorted count
    of given keywords """

    # Request titles one by one (using after and a limit)
    # using a custom user agent to avoid errors about 'too many requests'

    url = 'https://www.reddit.com/r/{}/hot.json?after={}&limit=1'.format(
        subreddit, after)

    headers = {'User-Agent': 'Nat'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    # If the resquest fail, do not run the rest of the code
    if r.status_code != 200:
        return

    data = r.json()['data']

    # If there are no more elements to check --> print!
    if len(data['children']) == 0:
        return to_text(hot_dict)

    # Get the tittle of this post and turn to lower case
    title = data['children'][0]['data']['title'].lower()

    # Split words of the title, put in a list to search easier
    title_words = title.split()

    # If a desired word is in the title --> Add count to the dictionary
    for w in word_list:
        word = w.lower()
        if title_words.count(word):
            if word in hot_dict:
                hot_dict[word] += title_words.count(word)
            else:
                hot_dict[word] = title_words.count(word)

    # Call this recursive function for the next reddit post
    after = data['after']
    count_words(subreddit, word_list, after, hot_dict)
