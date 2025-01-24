# Problem: Drop Duplicate Rows
# Question ID: 3071
# Difficulty: Easy
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/drop-duplicate-rows/

// https://leetcode.com/problems/drop-duplicate-rows

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset = 'email', keep = 'first', inplace = True)
    return customers
