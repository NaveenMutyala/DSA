class Solution:
    def mergeSort(self,nums,l,r):
        c=0
        if l>=r:
            return c
        m = (l+r)//2
        c += self.mergeSort(nums,l,m)
        c+= self.mergeSort(nums,m+1,r)
        c+=self.reverse(nums,l,m,r)
        self.merge(nums,l,m,r)
        return c
    def merge(self,nums,l,m,r):
        i = l
        j= m+1
        lt =[]
        while i<=m and j<=r:
            if nums[i]<nums[j]:
                lt.append(nums[i])
                i+=1
            else:
                lt.append(nums[j])
                j+=1
            
        while i<=m:
            lt.append(nums[i])
            i+=1
        while j <=r:
            lt.append(nums[j])
            j+=1
        for i in range(l,r+1):
            nums[i]=lt[i-l]
    def reverse(self,nums,l,m,r):
        c=0
        j= m+1
        for i in range(l,m+1):
            while j<=r and nums[i]>2*nums[j]:j+=1
            c+=j-(m+1)

        return c


    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums,0,len(nums)-1)



# 493. Reverse Pairs
# Solved
# Hard
# Topics
# Companies
# Hint
# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
