from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums)//2
        freq_arr = Counter(nums)
        for num,freq in freq_arr.items():
            if freq>half:
                return num
# 169. Majority Element
# Solved
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
