class Solution:
    def decodeAtIndex(self, inp: str, k: int) -> str:
        t=0

        for j in range(len(inp)):
            if inp[j].isdigit():
                t*=int(inp[j])
            else:
                t+=1
            if t>k:
                break    


        for i in range(j,-1,-1):
            if inp[i].isdigit():
                t = t//int(inp[i])
                k=k%t
            else:
                if k==0 or k==t:return inp[i]    

                t=t-1
