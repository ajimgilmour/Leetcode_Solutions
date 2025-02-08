# Problem: Design a Number Container System
# Question ID: 2434
# Difficulty: Medium
# Solved Date: 2025-02-08
# LeetCode URL: https://leetcode.com/problems/design-a-number-container-system/

// https://leetcode.com/problems/design-a-number-container-system

class NumberContainers:

    def __init__(self):
        self.mp = {}
        self.ind = {}

    def change(self, index: int, number: int) -> None:
        self.ind[index] = number
        if number not in self.mp:
            self.mp[number] = []
        heapq.heappush(self.mp[number], index) 

    def find(self, number: int) -> int:
        if number not in self.mp:
            return -1
        while self.mp[number]:
            m = self.mp[number][0]
            if self.ind.get(m) == number:
                return m
            heapq.heappop(self.mp[number])
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
