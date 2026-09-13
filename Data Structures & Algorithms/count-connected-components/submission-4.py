class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        h={i:[] for i in range(n)}
        visited=set()
        count=0
        
        for u,v in edges:
            h[u].append(v)
            h[v].append(u)
        
        def dfs(nei):
            if nei in visited:
                return
            visited.add(nei)
            for neighbour in h[nei]:
                dfs(neighbour)
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        return count