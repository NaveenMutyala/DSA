# print("Hello world")
lst =[1,2,3,4]
def f(ind,arr,s,k):
    if ind>=len(lst):
        if s==k:
            print(*arr)
        return
    arr.append(lst[ind])
    s+=lst[ind]
    f(ind+1,arr,s,k)
    s-=lst[ind]
    arr.pop()
    f(ind+1,arr,s,k)

f(0,[],0,3)
