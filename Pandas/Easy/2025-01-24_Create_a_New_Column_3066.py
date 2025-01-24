# Problem: Create a New Column
# Question ID: 3066
# Difficulty: Easy
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/create-a-new-column/

// https://leetcode.com/problems/create-a-new-column

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees
