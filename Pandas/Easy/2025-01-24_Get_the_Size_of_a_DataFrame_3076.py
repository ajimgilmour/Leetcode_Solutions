# Problem: Get the Size of a DataFrame
# Question ID: 3076
# Difficulty: Easy
# Solved Date: 2025-01-24
# LeetCode URL: https://leetcode.com/problems/get-the-size-of-a-dataframe/

// https://leetcode.com/problems/get-the-size-of-a-dataframe

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
