class Solution:
    def longestPalindrome(self, s: str) -> int:
        arr = [0]*60

        for i in s:
            a = ord(i) - 65
            arr[a]+=1

        ans = 0
        odd = False
        for i in arr:
            if i%2==1:
                odd = True
                ans += i-1
            else:
                ans+=i
        return ans + (1 if odd else 0)