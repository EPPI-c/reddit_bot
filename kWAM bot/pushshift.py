import requests
import time

class PushshiftConector:

    def __init__(self, subreddit) -> None:
        self.subreddit = subreddit
        self.posts_link = f'https://api.pushshift.io//reddit/search/submission/?subreddit={subreddit}'
        self.comments_link = f'https://api.pushshift.io//reddit/search/comment/?subreddit={subreddit}'
        self.meta = requests.get('https://api.pushshift.io/meta').json()
        self.rate_limit = 60/self.meta['server_ratelimit_per_minute']

    def get_post_after(self, after=None, fields=None) -> list:
        after = f'&after={after}' if after else ''
        fields = f'&fields=created_utc,{fields}' if fields else ''
        start = time.time()
        r = requests.get(f'{self.posts_link}{after}{fields}&size=500').json()['data']
        dur = time.time() - start
        res = [*r]
        while (len(r) > 0):
            if dur < self.rate_limit: time.sleep(dur)
            after = f'&after={res[-1]["created_utc"]}'
            start = time.time()
            r = requests.get(f'{self.posts_link}{after}{fields}&size=500').json()['data']
            res.extend(r)
            dur = time.time() - start
        return res