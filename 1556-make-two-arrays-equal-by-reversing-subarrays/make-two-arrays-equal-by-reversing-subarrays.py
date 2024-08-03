class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        d ={}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=0
            d[arr[i]]+=1
            if d[arr[i]] == 0:
                d.pop(arr[i])
            if target[i] not in d:
                d[target[i]]=0
            d[target[i]]-=1
            if d[target[i]] == 0:
                d.pop(target[i])
        return len(d)==0