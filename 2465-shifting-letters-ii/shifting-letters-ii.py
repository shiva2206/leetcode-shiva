class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = [0]*(1+len(s))
        for i,j,k in shifts:
            
            if k==1:
                l[i]+=1
                l[j+1]-=1
            else:
                l[i]-=1
                l[j+1]+=1
            

        for i in range(1,len(l)):
            l[i]+= l[i-1]
            if l[i]>=26:
                l[i]%=26
            elif l[i]<=-26:
                l[i] = -1*(-l[i]%26)
        res = ""
        for i in range(len(s)):
            p = ord(s[i]) + l[i]
            if p>122:
                p= 96+(p - 122)%26
            elif p<97:
                p = 123 - (97-p)%26
            res += chr(p)
        return res
