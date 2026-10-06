class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=defaultdict(list)
        count=0
        visited=set()

        if len(edges)>n-1 or len(edges)<n-1:
            return False

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            for nei in adj[n]:
                if nei not in visited:
                    dfs(nei)
            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        if count>1:
            return False
        return True