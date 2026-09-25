class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        rank=[1]*(n+1)
        parent=[i for i in range(n+1)]

        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
            
        def union(a,b):
            roota=find(a)
            rootb=find(b)

            if roota==rootb:
                return False
            
            if rank[roota]>rank[rootb]:
                parent[rootb]=roota
            elif rank[roota]<rank[rootb]:
                parent[roota]=rootb
            else:
                parent[roota]=rootb
                rank[rootb]+=1
            
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
        
