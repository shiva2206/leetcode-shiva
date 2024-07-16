# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if startValue == destValue:return ""
        d = {}
        self.start = None
        def dfs(t):
            if not t:return 
            if t.val == startValue:
                self.start = t
            if t.left:
                d[t.left.val] = t
                dfs(t.left)
            if t.right:
                d[t.right.val]=t
                dfs(t.right)
            return 
        dfs(root)
        vis = set()
        l = [(self.start,"")]

    
        while l:
            p = []
            for x,y in l:
                if x.val == destValue:return y
                if x.left and x.left.val not in vis:
                    vis.add(x.left.val)
                    p.append((x.left,y+"L"))
                
                if x.right and x.right.val not in vis:
                    vis.add(x.right.val)
                    p.append((x.right,y+"R"))

                if x.val in d and d[x.val].val not in vis:
                    vis.add(d[x.val].val)
                    p.append((d[x.val],y+"U"))
            l = p+[]
            p=[]
                            
        return ""

            

        
        