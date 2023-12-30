def findTriplets(arr, n, k):
    
    # Write your code here.
    # pass
    arr.sort()
    res = []
    for i in range(n-2):
        if (i==0 or (i>0 and arr[i]!=arr[i-1])):
            l = i+1
            h = n-1
            sm = K-arr[i]
            while l<h:
                if arr[l]+arr[h] == sm :
                    res.append([arr[i],arr[l],arr[h]])
                    while l<h and arr[l]==arr[l+1]: l+=1
                    while l<h and arr[h]==arr[h-1]: h-=1
                    l+=1
                    h-=1
                elif arr[l]+arr[h] >sm:
                    h-=1
                else:
                    l+=1
    return res
