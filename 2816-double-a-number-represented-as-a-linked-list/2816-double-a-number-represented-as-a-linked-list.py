# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        def dfs(t):
            if not t:return None
            
            dfs(t.next)
            c = 0
            if t.next:
                c = 1 if t.next.val>=10 else 0
                t.next.val = t.next.val%10
        
            t.val = t.val*2 + c
            return 
        dfs(head)
        if head.val<10:
            return head
        head.val = head.val%10
        ans = ListNode(1)
        
        ans.next = head
        return ans
                