# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        que = collections.deque([root])
        z=True
        while que:
            p = len(que)
            w = []
            for i in range(p):
                t = que.popleft()
                if not t.left:
                    z = False
                else:

                    if not z:return False
                    w.append(t.left.val)
                    que.append(t.left)
                if t.right :
                    if not z:return False
                    w.append(t.right.val)
                    que.append(t.right)
                else:
                    z = False
            print(w)
        return True