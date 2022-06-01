#!/usr/bin/python3

"""prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """
    Returns the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # pprint(data)
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
