# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        start = -1
        m = float('inf')
        p = -1
        prev = None
        b = 0
        while head:
            b+=1
            if prev and head.next:
                if prev.val<head.val>head.next.val:
                    if start == -1:
                        start = b
                    else:
                        m = min(m,b-p)
                        
                    p = b
                if prev.val>head.val<head.next.val:
                    if start == -1:
                        start = b
                    else:
                        m = min(m,b-p)
                    p = b
            prev = head
            head = head.next
        if start == p :return [-1,-1]
        return [m,p-start]


           
        if len(l)<2:return [-1,-1]
        l.sort()
        # print(l)
        a = l[1]-l[0]
        for i in range(2,len(l)):
            a = min(a,l[i] - l[i-1])
        return [a,l[-1]-l[0]]
