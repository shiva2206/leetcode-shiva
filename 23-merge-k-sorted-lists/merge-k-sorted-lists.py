# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        d = {}
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                d[i] = lists[i]
                pq.append((lists[i].val,i))
        heapq.heapify(pq)
        ans= ListNode(10)
        res = ans
        while pq:
            x,y = heapq.heappop(pq)
            ans.next = d[y]
            ans = ans.next
            if d[y].next:
                d[y] = d[y].next
                heapq.heappush(pq,(d[y].val,y))
        return res.next
        

