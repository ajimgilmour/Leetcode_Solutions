# Problem: Calculate Special Bonus
# Question ID: 2024
# Difficulty: Easy
# Solved Date: 2025-02-15
# LeetCode URL: https://leetcode.com/problems/calculate-special-bonus/

// https://leetcode.com/problems/calculate-special-bonus

import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = np.where(
        (employees['name'].str[0] != 'M') & (employees['employee_id'] % 2 != 0),
        employees['salary'],
        0
    )
    return employees[['employee_id', 'bonus']].sort_values('employee_id')

