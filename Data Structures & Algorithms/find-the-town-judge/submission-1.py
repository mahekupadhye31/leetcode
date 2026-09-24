class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting=defaultdict(list)
        trusted=defaultdict(list)

        for a,b in trust:
            trusting[a].append(b)
            trusted[b].append(a)
        
        for i in range(1,n+1):
            if len(trusting[i])==0:
                if len(trusted[i])==n-1:
                    return i
        return -1