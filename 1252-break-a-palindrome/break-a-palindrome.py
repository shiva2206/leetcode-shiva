class Solution:
    def breakPalindrome(self, pal: str) -> str:
        if len(pal)==1: return ""
        i = 0
        j = len(pal) -1

        while i<=j:
            if pal[i]=='a':
                i+=1
                j-=1
            elif i==j : return pal[:len(pal)-1] +'b'   
            else:    
                return pal[:i] + 'a' + pal[i+1:] 
        
        return "a"*(len(pal)-1) +'b'        