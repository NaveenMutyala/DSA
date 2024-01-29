def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # print(n)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k<l:
                    sum_ = nums[i]+ nums[j]+ nums[k]+nums[l]
                    # print(sum_)
                    if target == sum_:
                        temp =[nums[i],nums[j],nums[k],nums[l]]
                        # print(temp)
                        res.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]== nums[l+1]:
                            l-=1
                    elif target > sum_ :
                        k+=1
                    else:
                        l-=1
        return res



# 18. 4Sum
# Solved
# Medium
# Topics
# Companies
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
