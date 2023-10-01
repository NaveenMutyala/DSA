arr =[5,3,2,1,8,24,13]
def mergeSort(arr,l,r):
    # print("h")
    mid = (l+r)//2
    # print(l)
    # print(r)
    # print(mid)
    if l>=r:
        return
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)
        
def merge(arr,l,m,r):
    print(arr[l:r+1])
    print(l,r,m)
    i=l
    j=m+1
    temp=[]
    while i<=m and j<=r:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    if i<=m:
        for k in range(i,m+1):
            temp.append(arr[k])
    if j<=r:
        for k in range(j,r+1):
            temp.append(arr[k])
    k=0
    for i in range(l,r+1):
        arr[i]=temp[k]
        k+=1
        
mergeSort(arr,0,len(arr)-1)
print(arr)
