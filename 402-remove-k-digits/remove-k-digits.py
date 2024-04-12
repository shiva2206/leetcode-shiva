class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
         
        ans = []
        for i in num:
            i = int(i)
            while ans and ans[-1]>i and k>0:
                k-=1
                ans.pop()
            ans.append(i)
        
        while ans and k>0:
            ans.pop()
            k-=1

        for i in range(len(ans)):
            if ans[i]!=0:
                return "".join(map(str,ans[i:]))    
        return "0"