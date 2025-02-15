# Problem: Find the Punishment Number of an Integer
# Question ID: 2802
# Difficulty: Medium
# Solved Date: 2025-02-15
# LeetCode URL: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

// https://leetcode.com/problems/find-the-punishment-number-of-an-integer

class Solution:
    def punishmentNumber(self, n: int) -> int:
        total_sum = 0
        
        def can_partition_bitmask(num_str, target):
            n = len(num_str)
            total_partitions = 1 << (n - 1)

            for mask in range(total_partitions):  
                current_sum = 0
                part = 0  

                for i in range(n):  
                    part = part * 10 + int(num_str[i]) 
                    if mask & (1 << i) or i == n - 1:
                        current_sum += part  
                        part = 0
                
                if current_sum == target:
                    return True

            return False

        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition_bitmask(square_str, i):
                total_sum += i * i

        return total_sum

