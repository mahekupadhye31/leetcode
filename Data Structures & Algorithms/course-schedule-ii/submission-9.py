class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegrees=defaultdict(int)
        res=[]
        q=deque()

        for u,v in prerequisites:
            adj[v].append(u)
            indegrees[u]+=1
        
        for i in range(numCourses):
            if indegrees[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegrees[nei]-=1
                if indegrees[nei]==0:
                    q.append(nei)
        
        return res if len(res)==numCourses else []