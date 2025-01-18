# Problem: Minimum Cost to Make at Least One Valid Path in a Grid
# Question ID: 1485
# Difficulty: Hard
# Solved Date: 2025-01-18
# LeetCode URL: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        from collections import deque
        dq = deque([(0, 0)])
        m, n = len(grid), len(grid[0])
        mat = [[float('inf') for _ in range(n)] for _ in range(m)]
        mat[0][0] = 0
        direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        book = {(0, 1): 1, (0, -1): 2, (1, 0): 3, (-1, 0): 4}

        # BFS.
        while dq:
            x, y = dq.popleft()
            for dx, dy in direct:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    cost = book[(dx, dy)] != grid[x][y]
                    if mat[x+dx][y+dy] > mat[x][y] + cost:
                        dq.append((x+dx, y+dy))
                        mat[x+dx][y+dy] = mat[x][y] + cost
            
        return mat[-1][-1]      
