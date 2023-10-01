lst =[1,2,3,4]
def f(ind,arr,s,k):
    if ind>=len(lst):
        if s==k:
            print(*arr)
            return 1
        return 0
    arr.append(lst[ind])
    s+=lst[ind]
    l = f(ind+1,arr,s,k)
    s-=lst[ind]
    arr.pop()
    r = f(ind+1,arr,s,k)
    return l+r

print(f(0,[],0,3))
