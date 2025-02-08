# Problem: Find the Number of Distinct Colors Among the Balls
# Question ID: 3434
# Difficulty: Medium
# Solved Date: 2025-02-08
# LeetCode URL: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        bc = {}
        cc = {}
        c = set()
        res = []

        for i, j in queries:
            if i in bc:
                prev = bc[i]
                cc[prev] -= 1
                if cc[prev] == 0:
                    c.remove(prev)
            bc[i] = j
            cc[j] = cc.get(j, 0) + 1
            c.add(j)

            res.append(len(c))

        return res
