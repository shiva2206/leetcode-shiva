class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:return image
        tar = image[sr][sc]

        deq = deque([(sr,sc)])
        image[sr][sc]=color
        while deq:
            p = len(deq)
            for _ in range(p):
                i,j = deq.popleft()
                for k in [(0,1),(1,0),(-1,0),(0,-1)]:
                    x = i +k[0]
                    y = j +k[1]
                    if 0<=x<len(image) and 0<=y<len(image[x]) and image[x][y] == tar:
                        image[x][y] = color
                        deq.append((x,y))
        return image