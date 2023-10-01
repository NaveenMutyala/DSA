# print("Hello world")
lst =[1,2,3,4]
def f(ind,arr):
    if ind>=len(lst):
        print(*arr)
        return
    arr.append(lst[ind])
    f(ind+1,arr)
    arr.pop()
    f(ind+1,arr)

f(0,[])
