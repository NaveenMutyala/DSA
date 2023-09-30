def maxSubarraySum(arr, n) :

	# Your code here
    maxi = - float('inf')
    su=0
    # return the answerif
    for i in arr:
        su +=i
        
        if su <0:
            su=0  
        if maxi<su:
            maxi =su 
    return maxi


# Sample Input 1 :
# 9
# 1 2 7 -4 3 2 -10 9 1


# Sample Output 1 :
# 11
