class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        res=[]

        for a,b in prerequisites:
            adj[a].append(b)
            # adj[b].append(a)
        
        def dfs(u,v):
            if v in adj[u]:
                return True
            visited.add(u)
            for nei in adj[u]:
                if nei in visited:
                    continue
                if dfs(nei,v):
                    return True
            return False
        
        for u,v in queries:
            visited = set()
            res.append(dfs(u,v))
        return res