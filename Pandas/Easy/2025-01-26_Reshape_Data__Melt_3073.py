# Problem: Reshape Data: Melt
# Question ID: 3073
# Difficulty: Easy
# Solved Date: 2025-01-26
# LeetCode URL: https://leetcode.com/problems/reshape-data-melt/

// https://leetcode.com/problems/reshape-data-melt

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars = 'product', value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name = 'quarter', value_name = "sales")
