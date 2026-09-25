class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(set)
        result=[]

        for a,b in prerequisites:
            adj[a].add(b)

        def dfs(node,find):
            answer=False
            if node in visited:
                return False
            if find in adj[node]:
                return True

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    answer= answer or dfs(nei,find)
            return answer
        
        for node,find in queries:
            visited=set()
            ans=False

            if find in adj[node]:
                result.append(True)
            
            else:
                for nei in adj[node]:
                    if nei not in visited:
                        ans= ans or dfs(nei,find)
                        visited.add(nei)
            
                result.append(ans)
            
        return result