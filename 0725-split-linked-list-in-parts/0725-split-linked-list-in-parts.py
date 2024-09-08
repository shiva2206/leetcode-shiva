# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        n=0
        t=head
        while t:
            n+=1
            t=t.next
        rem = n%k
        t=head
        while head:
            
            for i in range(n//k):
                ptr=head
                head=head.next
            if rem!=0:
                rem-=1
                ptr=head
                head=head.next

            res.append(t)
            ptr.next=None
            t=head
        for i in range(k-len(res)):
            res.append(None)   
        return res    



        