# Problem: Rename Columns
# Question ID: 3068
# Difficulty: Easy
# Solved Date: 2025-01-25
# LeetCode URL: https://leetcode.com/problems/rename-columns/

// https://leetcode.com/problems/rename-columns

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(
        columns = {
            "id" : "student_id",
            "first" : "first_name",
            "last" : "last_name",
            "age" : "age_in_years",
        }
    )
    return students
