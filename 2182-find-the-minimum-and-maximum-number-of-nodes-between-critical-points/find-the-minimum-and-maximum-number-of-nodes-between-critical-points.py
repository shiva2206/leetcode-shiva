# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l = []
        prev = None
        b = 0
        while head:
            b+=1
            if prev and head.next:
                if prev.val<head.val>head.next.val:
                    l.append(b)
                    
                if prev.val>head.val<head.next.val:
                    l.append(b)
            prev = head
            head = head.next
        if len(l)<2:return [-1,-1]
        l.sort()
        # print(l)
        a = l[1]-l[0]
        for i in range(2,len(l)):
            a = min(a,l[i] - l[i-1])
        return [a,l[-1]-l[0]]
