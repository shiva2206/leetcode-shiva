class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res =[]
        def dfs(dig):
            if dig>n:return 
            res.append(dig)

            dig*=10
            for j in range(10):
                if dig==0 and j==0:
                    res.pop()
                    continue
                dfs(j + dig)
        dfs(0)

        return res