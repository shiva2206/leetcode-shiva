class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            arr = [0]*26
            for i in s:
                arr[ord(i)-97]+=1
            t = ",".join(map(str,arr))
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        return list(d.values())

