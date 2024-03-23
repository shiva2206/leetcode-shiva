# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:return head
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        fast = slow.next
        slow.next = None

        t = None
        while fast:
            q = fast.next
            fast.next = t
            t = fast
            fast = q
        ans = ListNode(0)
        d = ans
        while t:
            a = head.next
            b = t.next 
            head.next = t
            ans.next = head
            ans = t
            head = a
            t = b
        if head:
            ans.next = head

        return d.next    
                

