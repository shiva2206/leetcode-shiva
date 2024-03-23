class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

    def addNum(self, num: int) -> None:
         
        if self.min and num > self.min[0]:
            heapq.heappush(self.min,num)
            if len(self.min)>len(self.max):
                heapq.heappush(self.max,- heapq.heappop(self.min))
        else:
            heapq.heappush(self.max,- num)
            if len(self.max) == len(self.min)+2:
                heapq.heappush(self.min,- heapq.heappop(self.max))

        # print(self.max)
        # print(self.min)
        # print()
            

    def findMedian(self) -> float:
        if (len(self.min) + len(self.max))%2==0:
            return  (-self.max[0] + self.min[0])/2
        return - self.max[0]     


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()