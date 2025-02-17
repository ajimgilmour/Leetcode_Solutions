# Problem: Construct the Lexicographically Largest Valid Sequence
# Question ID: 1819
# Difficulty: Medium
# Solved Date: 2025-02-17
# LeetCode URL: https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        visited = set()
        length = (2 * n) - 1
        res = [0] * length
        def backtrack(index):
            if index == length:
                return True
            
            if res[index] != 0:
                return backtrack(index + 1)

            for j in range(n, 0, -1):
                if j in visited:
                    continue
                if j == 1:
                    res[index] = 1
                    visited.add(1)
                    if backtrack(index + 1):
                        return True
                    res[index] = 0
                    visited.remove(1)
                else:
                    second_pos = j + index
                    if second_pos < length and res[second_pos] == 0:
                        res[index] = j
                        res[second_pos] = j
                        visited.add(j)
                        if backtrack(index + 1):
                            return True
                        res[index] = 0
                        res[second_pos] = 0
                        visited.remove(j)
        backtrack(0)
        return res
