class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        for i in range(len(times)):
            times[i].append(i)
        
        times.sort()
        hp = []
        i=0
        left = []
        print(times)
        for start,end,num in times:
            if not left:
                left.append(i)
                i+=1
            while hp and hp[0][0]<=start:
                y = heapq.heappop(hp)[1]
                heapq.heappush(left,y)
        
            if num == targetFriend:return heapq.heappop(left)
            seat = heapq.heappop(left)
            heapq.heappush(hp,(end,seat))
            
        return -1

