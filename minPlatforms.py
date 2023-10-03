from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    # Write your code here.
    # pass
    at.sort()
    dt.sort()
    platforms=1
    mx=1
    i=1
    j=0
    while i<len(at) and j<len(at):
        if at[i]<=dt[j]:
            platforms+=1
            i+=1
        elif at[i]>dt[j]:
            platforms -=1
            j+=1
        mx= max(mx,platforms)
    return mx


# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)

# Sample Input 1:
# 2
# 6
# 900 940 950 1100 1500 1800
# 910 1200 1120 1130 1900 2000
# 4
# 100 200 300 400
# 200 300 400 500
# Sample Output 1:
# 3
# 2
