Jobs.sort(key=lambda x:x.profit ,reverse=True)
        mxd=0
        for i in Jobs:
            mxd=max(mxd,i.deadline)
        res=[-1]*(mxd+1)
        profit=0
        c=0
        for i in range(n):
            for j in range(Jobs[i].deadline,0,-1):
                if res[j]==-1:
                    res[j]=Jobs[i].profit
                    profit+=res[j]
                    c+=1
                    break
        arr=[c,profit]
        return arr
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
