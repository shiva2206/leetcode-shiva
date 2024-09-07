# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:return True
        if not root:return False
        def dfs(x,y):
            if not y:return True
            if not x : return False
            return x.val == y.val and (dfs(x.left,y.next) or dfs(x.right,y.next))
        
        def alcom(p,q):
            
            if dfs(p,q):return True
            if not p:return False
            return alcom(p.left,q) or alcom(p.right,q)
        
        return alcom(root,head)