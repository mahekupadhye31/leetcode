class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree=defaultdict(int)
        adj=defaultdict(set)
        
        for word in words:
            for ch in word:
                indegree[ch]=0
                adj[ch]=set()

        for i in range(len(words)-1):
            s1=words[i]
            s2=words[i+1]
            length=min(len(s1),len(s2))
            if len(s1)>len(s2) and s1.startswith(s2):
                return ""
            for j in range(length):
                if s1[j]!=s2[j]:
                    if s2[j] not in adj[s1[j]]: #eventho its a set we check so indegree for s2[j] isnt incremented again
                        adj[s1[j]].add(s2[j])
                        indegree[s2[j]]+=1
                    break
        
        q=deque()
        answer=[]
        #kahns algo to get the topo sort (relation ordering b/w nodes/letters)

        for ch in indegree:
            if indegree[ch]==0:
                q.append(ch)
        while q:
            letter=q.popleft()
            answer.append(letter)
            for nei in adj[letter]:
                indegree[nei]-=1
                if indegree[nei]==0: 
                    q.append(nei)
        return "".join(answer) if len(answer)==len(indegree) else ""