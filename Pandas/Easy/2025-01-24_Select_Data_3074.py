# Problem: Select Data
# Question ID: 3074
# Difficulty: Easy
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/select-data/

// https://leetcode.com/problems/select-data

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]
