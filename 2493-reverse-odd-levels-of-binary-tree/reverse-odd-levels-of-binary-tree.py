# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = deque()
        que.append(root)
        h = 0
        q = []
        while que:
            for i in range(len(que)):
                t = que.popleft()
                if h%2==1:
                    t.val = q.pop()
                if t.left:
                    que.append(t.left)
                    if h%2==0:
                        q.append(t.left.val)
                if t.right:
                    if h%2==0:
                        q.append(t.right.val)
                    que.append(t.right)
           
            h+=1
        return root