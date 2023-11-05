class Solution:
    def decodeAtIndex(self, inp: str, k: int) -> str:
        t=0
        for i in inp:
            if i.isdigit():
                t*=int(i)
            else:
                t+=1

        for i in range(len(inp)-1,-1,-1):
            if inp[i].isdigit():
                t = t//int(inp[i])
                k=k%t
            else:
                if k==0 or k==t:return inp[i]    

                t=t-1
                