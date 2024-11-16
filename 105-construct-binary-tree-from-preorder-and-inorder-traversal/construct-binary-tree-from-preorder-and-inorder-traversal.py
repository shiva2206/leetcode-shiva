# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i
        
        def construct(x,y,i,j):
        
            if i == j:return TreeNode(inorder[i])
            if x>y:return None
            t = TreeNode(preorder[x])
            p = d[preorder[x]]
            t.left = construct(x+1,x+(p-i),i,p-1)

            t.right = construct(x+(p-i)+1,y,p+1,j)
            return t
        return construct(0,len(preorder)-1,0,len(inorder)-1)
        