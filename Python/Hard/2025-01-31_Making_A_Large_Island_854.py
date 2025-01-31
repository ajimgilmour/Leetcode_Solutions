# Problem: Making A Large Island
# Question ID: 854
# Difficulty: Hard
# Solved Date: 2025-01-31
# LeetCode URL: https://leetcode.com/problems/making-a-large-island/

// https://leetcode.com/problems/making-a-large-island

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        visited = []
        for i in range(n):
            visited.append([False]*n)
        
        island_id = []
        for i in range(n):
            island_id.append([0]*n)
            
        
        def dfs(i, j, idx):
            visited[i][j] = True
            island_id[i][j] = idx
            if i > 0 and visited[i-1][j] == False and grid[i-1][j] == 1:
                dfs(i-1, j, idx)
            if i < n-1 and visited[i+1][j] == False and grid[i+1][j] == 1:    
                dfs(i+1, j, idx)
            if j > 0 and visited[i][j-1] == False and grid[i][j-1] == 1:    
                dfs(i, j-1, idx)
            if j < n-1 and visited[i][j+1] == False and grid[i][j+1] == 1:    
                dfs(i, j+1, idx)
        
        idx = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    idx += 1
                    dfs(i, j, idx)    
        
        size = defaultdict(int)
        for i in range(n):
            for j in range(n):
                size[island_id[i][j]] += 1
        
        max_size = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    if i > 0 and grid[i-1][j] == 1:
                        neighbors.add(island_id[i-1][j])
                    if i < n-1 and grid[i+1][j] == 1:
                        neighbors.add(island_id[i+1][j])
                    if j > 0 and grid[i][j-1] == 1:
                        neighbors.add(island_id[i][j-1])
                    if j < n-1 and grid[i][j+1] == 1:
                        neighbors.add(island_id[i][j+1])
                    
                    m = 0
                    for idx in neighbors:
                        m += size[idx]
                    max_size = max(max_size, min(m+1, n*n))    
        
        if max_size == 0:
            max_size = n*n
        
        return max_size
