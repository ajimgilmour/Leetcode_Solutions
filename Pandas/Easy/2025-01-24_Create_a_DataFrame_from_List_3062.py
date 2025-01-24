# Problem: Create a DataFrame from List
# Question ID: 3062
# Difficulty: Easy
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/create-a-dataframe-from-list/

// https://leetcode.com/problems/create-a-dataframe-from-list

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(data = student_data, columns = ['student_id', 'age'])
