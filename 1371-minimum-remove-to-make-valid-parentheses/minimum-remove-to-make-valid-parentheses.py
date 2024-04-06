class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p = 0

        res = ""
        for i in s:
            if i=="(":
                p+=1
            elif i==")":
                if p==0:
                    continue
                p-=1
            res+=i
        ans = ""
        for i in res[::-1]:
            if i=="(":
                if p!=0:
                    p-=1
                    continue
            ans += i
        return ans[::-1]
                


                

   