# Problem: Most Profitable Path in a Tree
# Question ID: 2564
# Difficulty: Medium
# Solved Date: 2025-02-24
# LeetCode URL: https://leetcode.com/problems/most-profitable-path-in-a-tree/

// https://leetcode.com/problems/most-profitable-path-in-a-tree

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_time = [n] * n
        def find_bob_path(node, prev, time): 
            if node == 0: 
                bob_time[node] = time
                return True
            for nxt in graph[node]:
                if nxt != prev and find_bob_path(nxt, node, time + 1): 
                    bob_time[node] = time
                    return True
            return False
        find_bob_path(bob, -1, 0)

        max_income = float('-inf')
        def find_alice_path(node, prev, time, income):
            if time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2 

            if node != 0 and len(graph[node]) == 1: 
                nonlocal max_income
                max_income = max(max_income, income)
                return 

            for nxt in graph[node]: 
                if nxt != prev: 
                    find_alice_path(nxt, node, time + 1, income)

        find_alice_path(0, -1, 0, 0)
        return max_income
        
