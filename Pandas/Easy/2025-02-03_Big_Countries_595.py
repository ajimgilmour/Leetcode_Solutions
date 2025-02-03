# Problem: Big Countries
# Question ID: 595
# Difficulty: Easy
# Solved Date: 2025-02-03
# LeetCode URL: https://leetcode.com/problems/big-countries/

// https://leetcode.com/problems/big-countries

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name','population','area']]
