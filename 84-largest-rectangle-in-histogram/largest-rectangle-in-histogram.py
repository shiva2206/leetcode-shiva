class Solution:
    def largestRectangleArea(self, hei: List[int]) -> int:
        
        
        sta = []
        ans = 0
        for i in range(len(hei)):
            x = i
            while sta and sta[-1][0]>=hei[i]:
                ans = max(ans,(i - sta[-1][1]) *sta[-1][0] )
                x = sta[-1][1]
                sta.pop()
            sta.append((hei[i],x))
     
        for h,i in sta:
            ans = max(ans,(len(hei) - i) * h)
        return ans