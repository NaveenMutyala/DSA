def MinimumCoins(n: int) -> List[int]:
    # write your code here
    # pass
    coins =[1000,500,100,50,20,10,5,2,1]
    con =[]
    for i in coins:
        if i<=n:
            temp = n//i
            n=n%i
            while temp>0:
                con.append(i)
                temp-=1
    return con

# Sample Input 1
# 13
# Sample Output 1
# 10 2 1
