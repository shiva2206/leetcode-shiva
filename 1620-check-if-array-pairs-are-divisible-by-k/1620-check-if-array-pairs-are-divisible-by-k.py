class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        d ={}
        for i in arr:
            a = i%k
            if a not in d:
                d[a]=1
            else:
                d[a]+=1
        if k%2==0 and k//2 in d and d[k//2]%2!=0:return False
        print("one")
        if 0 in d and d[0]%2!=0:return False
        print("two")
        print(d)
        for i in d.keys():
            if i!=0 and i!=k:
                if k-i not in d or d[k-i]!=d[i]:
                
                    return False
        print("three")
        return True