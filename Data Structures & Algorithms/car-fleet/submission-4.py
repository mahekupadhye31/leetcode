class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=[]
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))

        pairs.sort(reverse=True)

        stack=[]
        for p,s in pairs:
            time=(target-p)/s
            if stack and time<=stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)



