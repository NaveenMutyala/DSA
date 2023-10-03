class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        if root is None:
            return []
        
        di={}
        # code here
        q=[[root,0]]
        while q:
            node = q.pop(0)
            if node[1] not in di.keys():
                di[node[1]]=node[0].data
            if node[0].left != None:
                q.append([node[0].left,node[1]-1])
            if node[0].right!=None:
                q.append([node[0].right,node[1]+1])
            
        li = list(di.keys())
        li.sort()
        res = [di[i] for i in li]
        return res
