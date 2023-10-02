def subarrayWithMaxProduct(arr : List[int]) -> int:
    # Write your code here.
    # pass
    left =1
    right =1
    result =1
    for i in range(len(arr)):
        if left ==0:
            left =1
        if right==0:
            right =1
        left*=arr[i]
        right*=arr[len(arr)-i-1]
        result = max(result,max(left,right))
    return result



# or

  def subarrayWithMaxProduct(arr : List[int]) -> int:
    # Write your code here.
    # pass
    prod1=arr[0]
    prod2= arr[0]
    res=arr[0]
    for i in range(1,len(arr)):
        temp = max(arr[i],arr[i]*prod1,arr[i]*prod2)
        prod2 = min(arr[i],arr[i]*prod1,arr[i]*prod2)
        prod1 =temp
        res = max(res,prod1)
    return res

# Sample Input 1:
# 4
# 1 -2 3 -4
# Sample Output 1:
# 24
