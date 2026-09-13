class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        h=defaultdict(list)
        #h={i:[] for i in range(numCourses)}
        indegree={i:0 for i in range(numCourses)}
        answer=[]

        for u,v in prerequisites:
            h[v].append(u)
            indegree[u]+=1

        q=deque()
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            answer.append(node)
            for nei in h[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                    
        return answer if len(answer)==numCourses else []
