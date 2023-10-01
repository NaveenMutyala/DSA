class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.h=[]
        self.picking(0,candidates,[],target)
        return self.h
    def picking(self,i,arr,a,target):
        if i==len(arr):
            if target==0:
                self.h.append(a[:])
            return 
        if arr[i]<=target:
            a.append(arr[i])
            self.picking(i,arr,a,target-arr[i])
            a.pop()
        self.picking(i+1,arr,a,target)



# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 
