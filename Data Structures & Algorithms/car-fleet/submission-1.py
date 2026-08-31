class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        arrivalTimes=[0]*len(position)
        cars = sorted(zip(position, speed), reverse=True)
        for i in range(len(cars)):
            arrivalTimes[i]=(target-cars[i][0])/cars[i][1]
        
        stack.append((target-cars[0][0])//cars[0][1])
        for i in range(1,len(arrivalTimes)):
            if arrivalTimes[i]>stack[-1]:
                stack.append(arrivalTimes[i])
        
        return len(stack)
