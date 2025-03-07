# Problem: Closest Prime Numbers in Range
# Question ID: 2610
# Difficulty: Medium
# Solved Date: 2025-03-07
# LeetCode URL: https://leetcode.com/problems/closest-prime-numbers-in-range/

// https://leetcode.com/problems/closest-prime-numbers-in-range

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = []

        if right < 2:
            return [-1, -1]

        prime = [True] * (right + 1)
        prime[0] = prime[1] = False

        for i in range(2, right + 1):
            if prime[i]:
                for j in range(i * i, right + 1, i):
                    prime[j] = False

        primes = [i for i in range(left, right + 1) if prime[i]]
        
        if len(primes) < 2:
            return [-1, -1]

        closest_pair = [primes[0], primes[1]]
        min_diff = closest_pair[1] - closest_pair[0]

        for i in range(1, len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair
