# Problem: Fix Names in a Table
# Question ID: 1811
# Difficulty: Easy
# Solved Date: 2025-02-15
# LeetCode URL: https://leetcode.com/problems/fix-names-in-a-table/

// https://leetcode.com/problems/fix-names-in-a-table

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].apply(lambda x: x.capitalize())
    return users.sort_values('user_id')

