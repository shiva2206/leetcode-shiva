class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-97]+=1
            
            k = ",".join(map(str,arr))
            if k not in d:
                d[k] = [i]
            else:
                d[k].append(i)
        return list(d.values())