# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        t=head
        while head and head.next:
            x=head
            y=head.next
            z=gcd(head.val,head.next.val)
            
            x.next=ListNode(z)
            x.next.next=y
            head=y
        return t    
        
        
    