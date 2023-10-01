arr =[5,3,2,1,8,24,13]
def quickSort(arr,l,h):
    
    if l<h:
        p = partition(arr,l,h)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,h)
    
def partition(arr,l,h):
    pivot = l
    i = l
    j=h
    while i<j:
        while i<=h and arr[pivot]>=arr[i]  :
            i+=1
        while j>=l and arr[pivot]<arr[j] :
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
        
    arr[j],arr[pivot] = arr[pivot],arr[j]
    print(arr)
    return j
quickSort(arr,0,6)
print(arr)
