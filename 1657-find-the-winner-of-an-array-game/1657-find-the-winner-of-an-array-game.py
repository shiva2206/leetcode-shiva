class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        m=arr[0]
        d=defaultdict(int)
        c=0
        for i in range(1,len(arr)):
            if m<arr[i]:
                m=arr[i]
                c=0
            c+=1
            if c==k:return m
          
        return m         

                
        