class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
       d=defaultdict(list)
       for i in edges:
           d[i[0]].append(i[1:])

       
       par=[i for i in range(n+1)]
       ran=[1 for i in range(n+1)]

       def find(x):
           while x!=par[x]:
               x=par[x]
               par[x]=par[par[x]]

           return x

       def union(x,y):
           p1,p2=find(x),find(y)

           if p1==p2:
               return False
           if ran[p1]<ran[p2]:
               ran[p2]+=ran[p1]
               par[p1]=p2
           else:
               ran[p2]+=ran[p1]
               par[p2]=p1
           return True
       self.res=n;

       self.t=0 
       def dfs(i):
           
           for p in d[i]:
             
               if self.res==1:
                  self.t+=1
               else:    
                  if union(p[0],p[1]):  
                    self.res-=1
                  else:
                    self.t+=1   
       dfs(3) 
       
       if self.res==1:
           return len(d[1])+len(d[2])+self.t
       rank=ran+[]
       part=par+[]
       w=self.res
       dfs(2)
       
       if self.res!=1:
           return -1
       ran[:]=rank+[]
       par[:]=part+[]
       self.res=w
       dfs(1)
       
       if self.res!=1:
           return -1 
         
       return self.t;

