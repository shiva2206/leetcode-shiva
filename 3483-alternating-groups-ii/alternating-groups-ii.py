class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k ==1:return len(colors)
        ans = 0
        i = 0
        for j in range(1,len(colors)):
            
            if colors[j] == colors[j-1]:
                i = j
            if j - i +1<k:
                continue
            ans+=1
            print(i)
            i+=1
        if colors[-1]==colors[0] :return ans
    
        if len(colors) - i +1 ==k:
            ans+=1
            i+=1
        for j in range(1,len(colors)):
            if colors[j] == colors[j-1]:return ans
            if len(colors) - i + j+1<k:
                continue
            ans +=1
            print(i)
            i+=1
            if i==len(colors):return ans
                
        return ans 
         