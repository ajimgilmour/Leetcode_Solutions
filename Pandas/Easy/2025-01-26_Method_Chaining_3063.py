# Problem: Method Chaining
# Question ID: 3063
# Difficulty: Easy
# Solved Date: 2025-01-26
# LeetCode URL: https://leetcode.com/problems/method-chaining/

// https://leetcode.com/problems/method-chaining

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by = 'weight', ascending = False)[['name']]
