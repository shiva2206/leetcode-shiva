# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        stack = [(root,1)]
        inorder = []

        while stack :
            node,val = stack.pop()
            if val==1:
                stack.append((node,2))
                if node.left:
                    stack.append((node.left,1))
            elif val==2:
                stack.append((node,3))
                inorder.append(node.val)
                if node.right:
                    stack.append((node.right,1))
        return inorder
