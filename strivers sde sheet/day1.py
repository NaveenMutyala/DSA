def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while nums[i]>=nums[i+1] and i>=0:
            i-=1
        if i>=0:
            j = len(nums)-1
            while nums[i]>=nums[j]:
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        def reverse(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        reverse(i+1,len(nums)-1)
        return nums

# kadane algorith
def maxSubArray(self, nums: List[int]) -> int:
        dp =[0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low =0
        mid = 0
        high = len(nums)-1
        while mid<= high:
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]= nums[high],nums[mid]
                high-=1

def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        res =-float('inf')
        for i in prices:
            mini  = min(i,mini)
            res = max(res,i-mini)
        return res
# rotote 90
def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix)
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]


 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        # intervals.sort(key=lambda x:x[-1])
        res =[]
        flag =False
        temp =intervals[0]
        for i in range(1,len(intervals)):
            if temp[-1]>=intervals[i][0]:
                temp[0] = min(temp[0],intervals[i][0])
                temp[-1] = max(temp[-1],intervals[i][-1])
            else:
                res.append(temp)
                temp = intervals[i]
        res.append(temp)
            
        return res
   # or
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans =[]
        intervals.sort()
        for i in range(len(intervals)):
            if not ans or ans[-1][-1]<intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][-1] = max(ans[-1][-1],intervals[i][-1])
        return ans

