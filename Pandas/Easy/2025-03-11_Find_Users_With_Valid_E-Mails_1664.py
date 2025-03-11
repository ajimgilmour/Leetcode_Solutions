# Problem: Find Users With Valid E-Mails
# Question ID: 1664
# Difficulty: Easy
# Solved Date: 2025-03-11
# LeetCode URL: https://leetcode.com/problems/find-users-with-valid-e-mails/

// https://leetcode.com/problems/find-users-with-valid-e-mails

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[A-Za-z][-._A-Za-z0-9]*@leetcode\.com$"
    filterr = users['mail'].str.match(pattern)
    df = users[filterr]
    return df
