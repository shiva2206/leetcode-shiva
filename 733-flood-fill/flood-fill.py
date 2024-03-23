class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:return image    
        self.tar = image[sr][sc]
        def dfs(i,j):
            if 0<=i<len(image) and 0<=j<len(image[i]) and self.tar == image[i][j]:
                image[i][j] = color
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)
        dfs(sr,sc)        
        return image        
                