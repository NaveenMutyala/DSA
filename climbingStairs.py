def climbStairs(self, n: int) -> int:
        c=[1,2]
        if n<=2:
            return n
        else:
            for i in range(3,n+1):
                tm=sum(c)
                c[0],c[1]=c[1],tm
        return c[1]

# or

def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    dp=[-1]*(nStairs+1)
    if nStairs<2:
        return 1
    dp[0]=1
    dp[1]=1
    for i in range(2,nStairs+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[nStairs]%(10**9 +7)


# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
