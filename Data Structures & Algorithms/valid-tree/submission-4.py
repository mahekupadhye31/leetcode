class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #we can use kahn's algorithm for directed acyclic graph
        # but this is an undirected graph so can we use kahns??
        # we cant use kahns as it relies on indegrees
        # a valid tree should be connected and not have cycles
        # a tree with n nodes, can only have n-1 edges for it to be a valid tree
        visited=set()
        h=defaultdict(list)

        if len(edges)!=n-1:
            return False
        
        for u,v in edges:
            h[u].append(v)
            h[v].append(u)
        
        def dfs(node,parent):
            visited.add(node)
            for nei in h[node]:
                if nei==parent:
                    continue
                if nei in visited and nei!=parent:
                    return False

                if not dfs(nei,node):
                    return False
            return True
                    
        if not dfs(0,-1):
            return False
        return len(visited)==n