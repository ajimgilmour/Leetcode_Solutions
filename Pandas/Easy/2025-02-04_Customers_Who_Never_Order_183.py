# Problem: Customers Who Never Order
# Question ID: 183
# Difficulty: Easy
# Solved Date: 2025-02-04
# LeetCode URL: https://leetcode.com/problems/customers-who-never-order/

// https://leetcode.com/problems/customers-who-never-order

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    return df[['name']].rename(columns={'name':'Customers'})
