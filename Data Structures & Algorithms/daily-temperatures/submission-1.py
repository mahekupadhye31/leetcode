class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # basically we want to find the next greater element
        # for next greater element we keep a monotonic decreasing stack
        #[5,4,2,1]
        n=len(temperatures)
        stack=[]
        results=[0]*n

        for i,temp in enumerate(temperatures):
            # if len(stack)==0:
            #     stack.append(i)
            while stack and temp>temperatures[stack[-1]]:
                prev_index=stack.pop()
                results[prev_index]=(i-prev_index)
                # stack.append(i)
            stack.append(i)
        return results