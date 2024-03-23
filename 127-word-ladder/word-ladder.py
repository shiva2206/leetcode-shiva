class Solution:
    def ladderLength(self, begin: str, end: str, word: List[str]) -> int:
        if begin==end : return 1
        d = {}
        z = False
        for i in word:
            for j in range(len(i)):
                s = i[:j] + "*" + i[j+1:]
                if s not in d:
                    d[s]=[]
                d[s].append(i)
            if i==end:z=True
        if not z:return 0        
        t = 1
        

        deq = deque([begin])
        while deq:
            p = len(deq)
            print(deq)
            for _ in range(p):
                k = deq.popleft()

                for x in range(len(k)):
                    s = k[:x] +"*" + k[x+1:]
                    if s in d:
                        for kk in d[s]:
                            deq.append(kk)
                            if kk==end:return t+1
                        d.pop(s)        
            t+=1
        return 0                

                    