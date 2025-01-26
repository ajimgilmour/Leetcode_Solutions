# Problem: Reshape Data: Pivot
# Question ID: 3072
# Difficulty: Easy
# Solved Date: 2025-01-26
# LeetCode URL: https://leetcode.com/problems/reshape-data-pivot/

// https://leetcode.com/problems/reshape-data-pivot

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    final = weather.pivot(index = 'month', columns = 'city', values = 'temperature')
    return final
