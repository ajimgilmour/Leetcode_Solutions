# Problem: Reshape Data: Concatenate
# Question ID: 3064
# Difficulty: Easy
# Solved Date: 2025-01-26
# LeetCode URL: https://leetcode.com/problems/reshape-data-concatenate/

// https://leetcode.com/problems/reshape-data-concatenate

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis = 0)
