# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l=[]
        t = head
        while t:
            while l and l[-1]<t.val:
                l.pop()
            l.append(t.val)
            t = t.next
        ans = ListNode(0)
        t = ans
        i = 0
        while i<len(l):
            if l[i] == head.val:
                ans.next = head
                ans = ans.next
                i+=1

            head = head.next
        return t.next         
