# Problem: Invalid Tweets
# Question ID: 1827
# Difficulty: Easy
# Solved Date: 2025-02-06
# LeetCode URL: https://leetcode.com/problems/invalid-tweets/

// https://leetcode.com/problems/invalid-tweets

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    return df[['tweet_id']]
