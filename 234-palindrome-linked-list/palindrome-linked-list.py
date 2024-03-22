# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:return True
        slow = head
        fast = head.next

        t = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        t = None
        fast = slow.next
        slow.next = None

        while fast:
            q = fast.next
            fast.next = t
            t = fast
            fast = q
        # print(t.val)    
        # z = t
        # while z:
        #     print(z.val,end=" ")
        #     z = z.next
        # y = head
        # print()
        # while y:
        #     print(y.val,end=" ")
        #     y = y.next    
        while t :
            if t.val!=head.val:return False
            t = t.next
            head = head.next
        return True        