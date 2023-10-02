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

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
