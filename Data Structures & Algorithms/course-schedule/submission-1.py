class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h=defaultdict(list)
        #h={i:[] for i in range(numCourses)}
        indegree={i:0 for i in range(numCourses)}

        for u,v in prerequisites:
            h[v].append(u)

        for i in range(numCourses):
            for nei in h[i]:
                indegree[nei]+=1
        
        q=deque()
        count=0

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                count+=1
        
        while q:
            node=q.popleft()
            for nei in h[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    count+=1
        return count==numCourses
