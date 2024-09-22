class Solution:
    def diffWaysToCompute(self, arr: str) -> List[int]:
        
        def cal(x,y,p):
            z = []
            for a in x:
                for b in y:
                    if p=="-":
                        z.append(a-b)
                    elif p=="+":
                        z.append(a+b)
                    else:
                        z.append(a*b)
            return z

        
        d = {}
        def dfs(i,j):
            if i>j:return []
            print(i,j)
            if i==j:return [int(exp[i])]
            if (i,j) in d:return d[(i,j)]
            l = []
            for k in range(i,j-1,2):
                x = dfs(i,k)
                y = dfs(k+2,j)
                if exp[k+1] == "-":
                    l.extend(cal(x,y,"-"))
                elif exp[k+1] == '+':
                    l.extend(cal(x,y,"+"))
                else:
                    l.extend(cal(x,y,"*"))
            d[(i,j)] = l
            return l
        import re 
        
        exp = re.split(r'([*+-])',arr)
        print(exp)
        return dfs(0,len(exp)-1)
