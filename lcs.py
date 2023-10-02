
from sys import stdin

def f(l,r,s,t,dp):
    if l<=0 or r<=0:
        return 0
    if dp[l][r]!=-1:
        return dp[l][r]
    if s[l-1]==t[r-1]:
        dp[l][r] = 1+f(l-1,r-1,s,t,dp)
        return dp[l][r]
    dp[l][r]= max(f(l-1,r,s,t,dp),f(l,r-1,s,t,dp))
    return dp[l][r]

def lcs(s, t) :
	#Your code goes here
    # arr=[[0 for _ in range(len(t)+1)] for i in range(len(s)+1)]
    # for i in range(1,len(s)+1):
    #     for j in range(1,len(t)+1):
    #         if s[i-1]==t[j-1]:
    #             arr[i][j]=arr[i-1][j-1]+1
    #         else:
    #             arr[i][j]=max(arr[i][j-1],arr[i-1][j])
    # return arr[-1][-1]

    dp=[[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0]=0
    for j in range(len(t)+1):
        dp[0][j]=0
    # return f(len(s),len(t),s,t,dp)

    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[len(s)][len(t)]

#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))
