arr=[1,2,3]
N= len(arr)
def palindrome(a,freq):
    if len(a)==N:
        print(*a)
        return
    for i in range(N):
        if not freq[i]:
            freq[i]=True
            palindrome(a+[arr[i]],freq)
            freq[i]=False
            
freq=[False]*len(arr)
palindrome([],freq)

# or

arr=[1,2,3]
N= len(arr)
def palindrome(ind):
    if ind==N:
        print(*arr)
        return
    for i in range(ind,N):
        arr[ind],arr[i]=arr[i],arr[ind]
        palindrome(ind+1)
        arr[ind],arr[i]=arr[i],arr[ind]
  
palindrome(0)

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
