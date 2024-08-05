class Solution:
    def kthDistinct(self, arr: List[str], n: int) -> str:
        l ={}
        for a in arr:
            
            if a not in l:
                l[a] = True
            elif l[a]:
                l[a]=False
        k = 0
        for a in arr:
            # a = ord(i)-97
            if l[a]:
                k+=1
                if k==n:return a
        return ""