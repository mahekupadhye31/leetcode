class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #we can use kahn's algorithm for directed acyclic graph
        # but this is an undirected graph so can we use kahns??
        # we cant use kahns as it relies on indegrees
        # a valid tree should be connected and not have cycles
        # a tree with n nodes, can only have n-1 edges for it to be a valid tree
        
        if len(edges)<n-1:
            return False
        
        adj={i: [] for i in range(n)}
        visited=set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count=0

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
            return 

        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1

        if count==1 and len(edges)==n-1:
            return True
        return False
