# Problem: Drop Missing Data
# Question ID: 3075
# Difficulty: Easy
# Solved Date: 2025-01-25
# LeetCode URL: https://leetcode.com/problems/drop-missing-data/

// https://leetcode.com/problems/drop-missing-data

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(axis = 0, how = 'all', subset = 'name', inplace = False)
