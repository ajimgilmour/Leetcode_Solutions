# Problem: Fill Missing Data
# Question ID: 3070
# Difficulty: Easy
# Solved Date: 2025-01-25
# LeetCode URL: https://leetcode.com/problems/fill-missing-data/

// https://leetcode.com/problems/fill-missing-data

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace = True)
    return products
