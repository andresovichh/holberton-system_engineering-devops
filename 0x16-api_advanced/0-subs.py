#!/usr/bin/python3
"""this is a module that gets the number of
subscribers of a subreddit"""

import requests
from pprint import pprint


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of a subreddit.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # pprint(data)
        return data['data']['subscribers']
    else:
        return 0
