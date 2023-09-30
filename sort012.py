def sort012(arr, n) :
    low =0
    mid=0
    high = n-1
    while mid<=high:
        if arr[mid]==0:
            
            arr[low],arr[mid] = arr[mid],arr[low]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
            
	# write your code here
    # don't return anything 
    return arr


# Sample Input 1 :
# 2
# 6
# 0 1 2 2 1 0
# 7
# 0 1 2 1 2 1 2
# Sample Output 1 :
# 0 0 1 1 2 2
# 0 1 1 1 2 2 2
