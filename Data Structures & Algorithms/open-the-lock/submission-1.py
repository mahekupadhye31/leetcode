class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadSet=set(deadends)
        visited={"0000"}

        if '0000' in deadends:
            return -1
        if '0000'==target:
            return 0
        
        q=deque([('0000',0)])

        while q:
            code,turns=q.popleft()
            if code==target:
                return turns
            for i in range(4):
                digit1=str((int(code[i])+1)%10)
                digit2=str((int(code[i])-1)%10)
                new_code1= code[:i]+digit1+code[i+1:]
                new_code2= code[:i]+digit2+code[i+1:]
                if new_code1 not in deadSet and new_code1 not in visited:
                    q.append((new_code1,turns+1))
                    visited.add(new_code1)
                if new_code2 not in deadSet and new_code2 not in visited:
                    q.append((new_code2,turns+1))
                    visited.add(new_code2)
        return -1                