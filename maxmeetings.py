def maximumMeetings(start: List[int], end: List[int]) -> int:
    # write your code here
    # pass
    arr=[]
    for i in range(len(start)):
        arr.append([start[i],end[i],i+1])
    arr.sort(key=lambda x:x[1])
    li = -1*float('inf')
    res=[]
    for i in arr:
        if li<i[0]:
            res.append(i[-1])
            li=i[1]
        
    return len(res)

# Sample Input 1:
# 6
# 1 3 0 5 8 5
# 2 4 6 7 9 9
# Sample Output 1:
# 4
