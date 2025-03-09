class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k==1:return len(colors)
        ans = 0
        i = 0
        for x in range(1,2*len(colors)):
            j = x%len(colors)
            if colors[j] == colors[j-1]:
                if x>=len(colors):break
                i = j
            if i>=len(colors): break
            if x - i +1 <k:
                continue
            ans += 1
            i+=1
        return ans
