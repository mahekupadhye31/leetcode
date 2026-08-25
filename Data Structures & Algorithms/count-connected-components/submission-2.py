class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visitSet=set()
        connections={i:[] for i in range(n)}
        for l,r in edges:
            connections[l].append(r)
            connections[r].append(l)

        def dfs(i):
            visitSet.add(i)
            for j in connections[i]:
                if j not in visitSet:
                    dfs(j)
            connections[i]=[] 
            return 
            
        counter=0
        for i in range(n):
            if i not in visitSet:
                dfs(i)
                counter+=1

        return counter

