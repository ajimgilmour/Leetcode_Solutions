# Problem: Patients With a Condition
# Question ID: 1670
# Difficulty: Easy
# Solved Date: 2025-02-15
# LeetCode URL: https://leetcode.com/problems/patients-with-a-condition/

// https://leetcode.com/problems/patients-with-a-condition

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients['conditions'].str.contains(r'(^DIAB1)|( DIAB1)')]
    return df
