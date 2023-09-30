def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.
    # pass

    n = len(A)
    i = n-2
    while  A[i]>=A[i+1] and i>=0:
        i-=1
    if i>=0:
        j=n-1
        while A[i]>=A[j]:
            j-=1
        A[i],A[j]=A[j],A[i]
    rev(A,i+1,n-1)
    
    return A

def rev(nums,i,j):
    while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

# input : 3
# 3 1 2
# output:
# 3 2 1
