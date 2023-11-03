class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        m=1
        for i in target:
            if i>m:res.extend(["Push","Pop"]*(i-m))
            res.append("Push")
            m=i+1
        return res    


    