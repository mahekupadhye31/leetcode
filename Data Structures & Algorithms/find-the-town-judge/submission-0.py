class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting=defaultdict(set)
        trusted=defaultdict(set)
        for a,b in trust:
            trusting[a].add(b) #a trusts b
            trusted[b].add(a) #b is trusted by a

        for i in range(1,n+1):
            if len(trusted[i])==n-1 and (i not in trusted[i]):
                if len(trusting[i])==0:
                    return i
        return -1