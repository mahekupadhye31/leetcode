class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited=set()
        if '0000' in deadends:
            return -1
        q=deque()
        q.append((0,'0000'))
        while q:
            steps,number=q.popleft()
            if number==target:
                return steps
            for i in range(4):
                digit=int(number[i])
                num1=number[:i]+str((digit+1)%10)+number[i+1:]
                num2=number[:i]+str((digit-1)%10)+number[i+1:]
                if num1 not in visited and num1 not in deadends:
                    q.append((steps+1,num1))
                    visited.add(num1)
                if num2 not in visited and num2 not in deadends:
                    q.append((steps+1,num2))
                    visited.add(num2)
        return -1