class LockingTree:

    def __init__(self, parent: List[int]):
        self.par = parent+[]
        self.loc = [-1]*len(parent)
        self.child = defaultdict(list)
        for i,j in enumerate(parent):
            self.child[j].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.loc[num]!=-1:return False
        self.loc[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.loc[num] != user: return False
        self.loc[num]  = -1
        return True


    def upgrade(self, num: int, user: int) -> bool:
        if self.loc[num]!=-1:return False
        
       

        def ans(x):
            if x==-1:return True
            if self.loc[x]!=-1:return False
            return ans(self.par[x])
        if not ans(num):return False
        
        def dfs(x):
            if self.loc[x]!=-1:return True
            for k in self.child[x]:
                if dfs(k):
                    
                    return True
            return False

        if not dfs(num): return False
        def change(x):
            self.loc[x] = -1
            for k in self.child[x]:
                change(k)
            return 
        change(num)
        self.loc[num] = user
        return True
        





# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)