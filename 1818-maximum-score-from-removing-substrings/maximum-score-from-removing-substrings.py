class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        l = []
        ans = 0

        for i in range(len(s)):
            
            if x>y:
                if l and l[-1] + s[i]=="ab":
                    l.pop()
                    ans+=x
                else:
                    l.append(s[i])
                
            elif x<y :
                if l and l[-1]+s[i]=="ba":
                    l.pop()
                    ans+=y
                else:
                    l.append(s[i])
            else:
                if l:
                    if l[-1]+s[i]=="ab":
                        l.pop()
                        ans+=x
                    elif l[-1]+s[i]=="ba":
                        l.pop()
                        ans+=y
                    else:
                        l.append(s[i])
                else:
                    l.append(s[i])
        q = []
        for i in l:
            if i not in ["a","b"]:
                q=[]
                continue
            if q:
                if q[-1]+i=="ab":
                    q.pop()
                    ans+=x
                elif q[-1]+i=="ba":
                    q.pop()
                    ans+=y
                else:
                    q.append(i)
            else:
                q.append(i)
                    

        return ans