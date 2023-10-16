from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:

    # Write your code here.
    # pass
    ans =set()
    arr.sort()
    def find(ind,ds):
        ans.add(tuple(ds))
        for i in range(ind,n):
            ds.append(arr[i])
            find(i+1,ds)
            ds.pop()
    find(0,[])

    return [list(x) for x in ans]


# Sample Input 1:
# 2
# 3
# 1 1 3
# 4
# 1 3 3 3
# Sample Output 1:
# 1
# 1 1
# 1 3
# 3
# 1 1 3

# 1
# 1 3
# 1 3 3
# 1 3 3 3 
# 3 
# 3 3
3 3 3
