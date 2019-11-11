import os
import json
from collections import defaultdict
from tweet.tweet import Tweet

ROOT_DATA = '../data/'

def preprocessing(file):
    tweets = defaultdict()
    root = None

    with open(os.path.join(ROOT_DATA, file), "r") as fd:
        for line in fd:
            jn = json.loads(line)

            id_str = jn['id_str']
            full_text = jn['full_text']
            created_at = jn['created_at']
            screen_name = jn['user']['screen_name']
            display_text_range = jn['display_text_range']
            in_reply_to_status_id_str = jn['in_reply_to_status_id_str']

            if not in_reply_to_status_id_str:
                root = id_str

            tweets[id_str] = Tweet(id_str=id_str,
                                   full_text=full_text,
                                   created_at=created_at,
                                   screen_name=screen_name,
                                   display_text_range=display_text_range,
                                   in_reply_to_status_id_str=in_reply_to_status_id_str
                                  )
    return tweets, root

def tree_create(tweets, root):
    r = defaultdict(list)
    
    for id_st, tweet in tweets.items():
        if tweet.in_reply_to_status_id_str:
            r[tweet.in_reply_to_status_id_str].append(tweet)
    
    for k, v in r.items():
        tweets[k].replies = v
    
    return tweets[root]
