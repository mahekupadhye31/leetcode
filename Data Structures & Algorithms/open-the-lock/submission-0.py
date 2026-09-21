class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        visited={"0000"}

        if '0000' in deadends:
            return -1
        if '0000'==target:
            return 0

        q=deque([('0000',0)])

        while q:
            combination,turns=q.popleft()
            if combination==target:
                return turns
            for i in range(4):
                digit=int(combination[i])
                d1=str((digit-1)%10)
                d2=str((digit+1)%10)
                temp1=combination[:i]+d1+combination[i+1:]
                temp2=combination[:i]+d2+combination[i+1:]
                if temp1 not in dead and temp1 not in visited:
                    q.append((temp1,turns+1))
                    visited.add(temp1)
                if temp2 not in dead and temp2 not in visited:
                    q.append((temp2,turns+1))
                    visited.add(temp2)
                
        return -1
        