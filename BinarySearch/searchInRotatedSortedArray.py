def search(self, nums: List[int], target: int) -> int:
        l= 0
        r = len(nums)-1
        while l<=r:
            m = l+(r-l)//2
            if nums[m]==target:
                return m
            
            # left sorted array
            if nums[l]<=nums[m]:
                if target > nums[m] or target < nums[l]:
                    l=m+1
                else:
                    r = m-1
            # right sorted array
            else:
                if target < nums[m] or target > nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1


You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 
