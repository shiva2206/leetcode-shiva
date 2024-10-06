class Solution:
    def areSentencesSimilar(self, sent1: str, sent2: str) -> bool:

       sent1 = sent1.split()
       sent2 = sent2.split()

       if len(sent1)<len(sent2):
            sent1,sent2 = sent2+[],sent1+[]
       
       d = set()
       def dfs(i,j):
            
            if i>j:return True
            if (i,j) in d:return False
            d.add((i,j))
            if sent2[i] == sent1[i] and dfs(i+1,j): return True
            if sent2[j]==sent1[len(sent1) - (len(sent2) - j )] and dfs(i,j-1):return True
            return False
       return dfs(0,len(sent2)-1)
    

            