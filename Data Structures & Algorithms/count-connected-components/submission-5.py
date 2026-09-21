class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        count=0

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=set()
        count=0

        def dfs(i):
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)
            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count