class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m=len(edges)
        visited=set()
        count=0
        if m>n-1:
            return False
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        
        return count==1 and m==n-1