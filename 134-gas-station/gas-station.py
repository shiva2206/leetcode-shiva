class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):return -1
        ans = 0
        s=0
        for i in range(len(gas)):
            s += gas[i]-cost[i]
            if s <0:
                ans = i+1
                s=0
        return ans        
