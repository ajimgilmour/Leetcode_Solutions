# Problem: Modify Columns
# Question ID: 3067
# Difficulty: Easy
# Solved Date: 2025-01-25
# LeetCode URL: https://leetcode.com/problems/modify-columns/

// https://leetcode.com/problems/modify-columns

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
