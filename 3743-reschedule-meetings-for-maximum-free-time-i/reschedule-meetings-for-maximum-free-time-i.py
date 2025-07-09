class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime.append(eventTime)
        endTime.append(eventTime)
        prefix = [0]
        for i in range(len(endTime)):
            prefix.append(prefix[-1] + endTime[i]- startTime[i])
        ans = 0
        print(prefix)
        p = 0
        for i in range(len(endTime)):
            if i + k >=len(endTime): break
            temp =  startTime[i+k] - (prefix[i+k] - prefix[i]) - p
            # print(i,temp)
            ans = max(ans,temp )
            p = endTime[i]
        return ans