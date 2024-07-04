# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        
        ynext = head 
        s = 0
        cur = head.next
        while cur:
            if cur.val == 0:
                if s !=0:
                    ynext.next.val = s
                    ynext  = ynext.next
                s = 0
            else:
                s = s+ cur.val
            cur = cur.next
        if ynext==head:return None
        ynext.next=None
        return head.next
                