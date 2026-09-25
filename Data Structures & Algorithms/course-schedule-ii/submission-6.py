class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegree={i:0 for i in range(numCourses)}
        result=[]

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]=1+indegree.get(u,0)

        q=deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            result.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0: 
                    q.append(nei)
        return result if numCourses==len(result) else []