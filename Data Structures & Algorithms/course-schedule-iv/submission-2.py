class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj={i:[] for i in range(numCourses)}
        visited=set()

        for u,v in prerequisites:
            adj[u].append(v)
        
        result=[]
        def dfs(a,b,visited):
            for nei in adj[a]:
                if nei==b:
                    return True
                if nei not in visited:
                    visited.add(nei)
                    if dfs(nei,b, visited):
                        return True
            return False

        for a,b in queries:
            visited={a}
            result.append(dfs(a,b,visited))
        return result