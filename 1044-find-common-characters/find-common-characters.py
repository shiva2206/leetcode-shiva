class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = [float('inf')]*26
        for i in range(len(words)):
            l = [0]*26
            for j in words[i]:
                l[ord(j) - 97]+=1
            for i in range(len(l)):
                arr[i] = min(arr[i],l[i])
        ans = []
        for i in range(len(arr)):
            if arr[i]!=float('inf'):
                ans.extend([chr(i+97)]*arr[i])
        return ans