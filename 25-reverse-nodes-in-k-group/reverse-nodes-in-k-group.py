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

        ans = None
        prev =None
        for i in range(n//k):
            t = None
            p = head
            
            for j in range(k):
               
                q = p.next
                p.next = t
                t = p
                p = q
            if not ans:
                ans = t
            else:
            # l.append((t,head))
                prev.next = t
            prev = head
            if i+1 == n//k:
                head.next = p
                return ans
            head = p
        
        
        for i in range(len(l)-1):
            l[i][1].next = l[i+1][0]
        
        return l[0][0]
            
