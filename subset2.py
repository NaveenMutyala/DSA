 def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds =[]
        def findSubsets(ind):
            ans.append(ds[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i] == nums[i-1]:
                    continue
                ds.append(nums[i])
                findSubsets(i+1)
                ds.pop()
        nums.sort()
        findSubsets(0)
        return ans

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
