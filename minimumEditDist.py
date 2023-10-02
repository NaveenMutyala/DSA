class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp=[[-1 for i in range(len(word2))] for j in range(len(word1))]
    
        def f(i,j,dp):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=-1 : 
                return dp[i][j]
            if word1[i]==word2[j]:
                
                dp[i][j] = 0+f(i-1,j-1,dp)

            else:
                dp[i][j] = 1+min(f(i-1,j-1,dp),f(i-1,j,dp),f(i,j-1,dp))

            return dp[i][j]
        return f(len(word1)-1,len(word2)-1,dp)


# or

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        


        dp=[[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[len(word1)][len(word2)]


# output

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 
