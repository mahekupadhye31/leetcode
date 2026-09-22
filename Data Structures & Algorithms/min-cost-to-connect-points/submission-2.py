class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap=[]
        summation=0
        n=len(points)

        parent=[i for i in range(n+1)]
        rank=[1 for i in range(n+1)]

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
            
            if rank[roota]<rank[rootb]:
                parent[roota]=rootb
            elif rank[roota]>rank[rootb]:
                parent[rootb]=roota
            elif rank[roota]==rank[rootb]:
                parent[roota]=rootb
                rank[rootb]+=1
            
            return True

        for i in range(n):
            xo=points[i][0]
            yo=points[i][1]

            for j in range(i+1,n):
                x=points[j][0]
                y=points[j][1]

                dist= abs(xo-x)+abs(yo-y)
                heapq.heappush(minheap,(dist,i,j))

        while minheap:
            dist,i,j=heapq.heappop(minheap)
            if union(i,j):
                summation+=dist
            
        return summation