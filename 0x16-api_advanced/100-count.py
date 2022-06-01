"""Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

Requirements:

Prototype: def count_words(subreddit, word_list)
Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
If word_list contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with java)
Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
Results are based on the number of times a keyword appears, not titles it appears in. java java java counts as 3 separate occurrences of java.
To make life easier, java. or java! or java_ should not count as java
If no posts match or the subreddit is invalid, print nothing.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.
"""
import requests as r

def count_words(subreddit, word_list):
    """this is a foo"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) \
        Gecko/20100101 Firefox/73.0"
        }
    param = {
        "after": "",
        "limit": 100,
    }
    response = r.get(url, headers=headers, params=param, allow_redirects=False)
    if response.status_code == 404:
        return None
    else:
        posts = response.json().get("data").get("children")
        hot_list = [post.get("data").get("title") for post in posts]
        after = response.json().get("data").get("after")
        if after is not None:
            count_words(subreddit, hot_list, after)
        return hot_list