class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prev = intervals[0][1]
        for i in range(1,len(intervals)):
            start,end = intervals[i]

            if prev<=start:
                prev = end
            else:
                ans+=1
                prev = min(prev,end)
        return ans
