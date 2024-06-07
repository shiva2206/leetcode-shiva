class Solution:
    def replaceWords(self, dic: List[str], sent: str) -> str:
        d = set(dic)
        l = []
        sent = sent.split()

        for i in sent:
            q = "" 
            for j in range(len(i)):
                q = q+i[j]
                if q in d:
                    l.append(q)
                    break
            else:
                l.append(i)
        return " ".join(l)
        