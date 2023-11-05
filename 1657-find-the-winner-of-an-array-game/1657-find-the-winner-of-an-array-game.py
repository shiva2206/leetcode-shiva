class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        m=arr[0]
        d=defaultdict(int)
        for i in range(1,len(arr)):
            if m<arr[i]:
                m=arr[i]
            d[m]+=1
            if d[m]==k:return m
        print(d)        
        return m         

                
        