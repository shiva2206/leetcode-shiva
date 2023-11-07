class ThroneInheritance:

    def __init__(self, kingName: str):
        self.d=defaultdict(list)
        self.k=kingName
        self.d[self.k]=[]        
        self.dea=set()
    def birth(self, parentName: str, childName: str) -> None:
       
        self.d[parentName].append(childName)


    def death(self, name: str) -> None:
        self.dea.add(name)

    def getInheritanceOrder(self) -> List[str]:
        
        def dfs(t):
            
            res=[t] if t not in self.dea else []
            for x in self.d[t]:
                res.extend(dfs(x))
            return res
        print(self.d)
        return dfs(self.k)    