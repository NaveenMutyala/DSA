# recursion bottom-up
from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.


for i in range(int(input())):
    n = int(input())
    w = [int(x) for x in input().split()]
    v = [int(x) for x in input().split()]
    W = int(input())
    dp=[[-1 for i in range(W+1)] for j in range(n)]
    # l=-1*float('inf')
    for i in range(n):
        dp[i][0]=0
    for j in range(W+1):
        dp[0][j]=0
    
    def f(ind,W,dp):
        if ind==0:
            if w[ind]<=W:
                return v[ind]
            else:
                return 0
        if dp[ind][W] != -1: return dp[ind][W]
        dp[ind][W]= f(ind-1,W,dp)
        l=-1*float('inf')
        if w[ind]<=W:
            dp[ind][W] =max(v[ind]+f(ind-1,W-w[ind],dp), dp[ind][W]) 
        
        return dp[ind][W]
    print(f(n-1,W,dp))

# or

# topdown tabular form


import sys

# Function to solve the 0/1 knapsack problem using dynamic programming.
def knapsack(wt, val, n, W):
    # Initialize a 2D DP array to store the maximum value for different capacities and items.
    dp = [[0 for i in range(W + 1)] for j in range(n)]
    
    # Base condition: Fill in the first row based on the capacity 'W'.
    for i in range(wt[0], W + 1):
        dp[0][i] = val[0]
        
    # Iterate through the items and capacities.
    for ind in range(1, n):
        for cap in range(W + 1):
            # Calculate the maximum value when the current item is not taken.
            not_taken = 0 + dp[ind - 1][cap]
            
            # Calculate the maximum value when the current item is taken (if its weight allows).
            taken = -sys.maxsize
            if wt[ind] <= cap:
                taken = val[ind] + dp[ind - 1][cap - wt[ind]]
                
            # Update the DP table with the maximum of not_taken and taken values.
            dp[ind][cap] = max(not_taken, taken)
    
    # The result is stored in the bottom-right cell of the DP array.
    return dp[n - 1][W]

def main():
    wt = [1, 2, 4, 5]
    val = [5, 4, 8, 6]
    W = 5
    n = len(wt)
                                 
    # Find and print the maximum value of items the thief can steal.
    print("The Maximum value of items the thief can steal is", knapsack(wt, val, n, W))


# Sample Input:
# 1 
# 4
# 1 2 4 5
# 5 4 8 6
# 5
# Sample Output:
# 13
