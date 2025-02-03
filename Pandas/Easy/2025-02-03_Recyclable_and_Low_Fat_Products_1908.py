# Problem: Recyclable and Low Fat Products
# Question ID: 1908
# Difficulty: Easy
# Solved Date: 2025-02-03
# LeetCode URL: https://leetcode.com/problems/recyclable-and-low-fat-products/

// https://leetcode.com/problems/recyclable-and-low-fat-products

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    data = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return data[['product_id']]
