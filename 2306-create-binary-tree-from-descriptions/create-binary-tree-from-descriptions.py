# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, desc: List[List[int]]) -> Optional[TreeNode]:

        d={}
        hs = set()
        for i in desc:
            if i[0] not in d:
                d[i[0]] = []
            d[i[0]].append(i[1:])
            hs.add(i[1])
        head = None
        for i in d.keys():
            if i not in hs:
                head = i
  

        def dfs(t):
            if t not in d:
                return TreeNode(t)
            h = TreeNode(t)
            for i in d[t]:
                if i[1]==1:
                    h.left = dfs(i[0])
                else:
                    h.right = dfs(i[0])
            return h
        print(head,hs)
        return dfs(head)
        
        