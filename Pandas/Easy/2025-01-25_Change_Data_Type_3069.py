# Problem: Change Data Type
# Question ID: 3069
# Difficulty: Easy
# Solved Date: 2025-01-25
# LeetCode URL: https://leetcode.com/problems/change-data-type/

// https://leetcode.com/problems/change-data-type

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students = students.astype({'grade' : int})
    return students
