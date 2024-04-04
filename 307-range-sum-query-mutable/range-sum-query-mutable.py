class Node:
    def __init__(self,val:int):
        self.data = val
        self.left = None
        self.right = None
class NumArray:

    def __init__(self, nums: List[int]):
        self.tot = len(nums)-1
        def dfs(i,j):
            if i==j:
                t = Node(nums[i])
                return t
            m = (i+j)//2
            t = Node(0)
            t.left = dfs(i,m)
            t.right = dfs(m+1,j)
            t.data = t.left.data + t.right.data
            return t
        self.head = dfs(0,len(nums)-1)    
          

    def update(self, index: int, val: int) -> None:
        def dfs(t,i,j):
            if j<index or index<i:return 
            if i == j == index:
                t.data = val
                return
            m = (i+j)//2
            dfs(t.left,i,m) 
            dfs(t.right,m+1,j)
            t.data = t.left.data + t.right.data
            
            return 
        dfs(self.head,0,self.tot)

                    

    def sumRange(self, left: int, right: int) -> int:
        
        def dfs(t,i,j):
            if j<left or right<i: return 0
            if left<=i<=j<=right:return t.data
            m = (i+j)//2
            return dfs(t.left,i,m) + dfs(t.right,m+1,j)
        return dfs(self.head,0,self.tot)     


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)