# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        n = 0
        t = head
        while t!=None:
            t = t.next
            n+=1
        l = []
        for i in range(n//k):
            t = None
            p = head
            prev = head
            for j in range(k):
               
                q = p.next
                p.next = t
                t = p
                p = q
            l.append((t,head))
            head = p
            if i+1 == n//k:
                l.append((p,None))
        for i in range(len(l)-1):
            l[i][1].next = l[i+1][0]
        
        return l[0][0]
            
