
def subsetSum(arr: List[int]) -> List[int]:
    # Write your code here.
    # pass
    ans = []
    n=len(arr)

    def subsetSumsHelper(ind: int, sum: int):
        if ind == n:
            ans.append(sum)
            return
        # element is picked
        subsetSumsHelper(ind + 1, sum + arr[ind])
        # element is not picked
        subsetSumsHelper(ind + 1, sum)
    subsetSumsHelper(0, 0)
    ans.sort()
    return ans


# Sample Input 1 :
# 3
# 1 2 3
# Sample Output 1 :
# 0 1 2 3 3 4 5 6
