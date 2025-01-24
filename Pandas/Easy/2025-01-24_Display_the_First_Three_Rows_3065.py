# Problem: Display the First Three Rows
# Question ID: 3065
# Difficulty: Easy
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/display-the-first-three-rows/

// https://leetcode.com/problems/display-the-first-three-rows

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return (employees[:3])
