class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        for i in range(1,len(chalk)):
            chalk[i]+=chalk[i-1]
        k = k%chalk[-1]
        if k==0:return 0

        i= 0
        j = len(chalk)-1

        ans = len(chalk)
        
        while i<=j:
            m = (i+j)//2
            
            if k<chalk[m]:
                ans = m
                j = m-1
            else:
                i = m +1
        return ans
