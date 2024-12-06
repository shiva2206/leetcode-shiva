class Solution:
    def romanToInt(self, s: str) -> int:
        k = 0
        ans = 0
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1,-1,-1):
            if d[s[i]]>=k:
                ans += d[s[i]]
                k = d[s[i]]
            else:
                ans -= d[s[i]]
            print(ans)
        return ans

            