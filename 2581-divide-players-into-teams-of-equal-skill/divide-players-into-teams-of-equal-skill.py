class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)
        if s%(len(skill)//2)!=0:return -1
        m = s//(len(skill)//2)
        d ={}
        for i in skill:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        ans = 0
        d={}
        for i in skill:
            if m-i in d:
                d[m-i]-=1
                if d[m-i]==0:
                    d.pop(m-i)
                ans += i*(m-i)
            else:
                if i not in d:
                    d[i]=0
                d[i]+=1
        if len(d)!=0:return -1
        return ans