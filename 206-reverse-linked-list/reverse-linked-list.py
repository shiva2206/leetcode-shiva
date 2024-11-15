# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = None
        p = head
        while p:
            q = p.next
            p.next = t
            t = p
            p = q
        return t
