# Problem: Article Views I
# Question ID: 1258
# Difficulty: Easy
# Solved Date: 2025-02-04
# LeetCode URL: https://leetcode.com/problems/article-views-i/

// https://leetcode.com/problems/article-views-i

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    uniq = sorted(df['author_id'].unique())
    res = pd.DataFrame({'id' : uniq})
    return res

