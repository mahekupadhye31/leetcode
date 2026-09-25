class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # to find out next increasing temp or greater temp we use a monotonically decreasing stack
        st=[]
        n=len(temperatures)
        result=[0]*n
        for i,temp in enumerate(temperatures):

            while st and temp>temperatures[st[-1]]:
                result[st[-1]]=i-st[-1]
                st.pop()
            
            st.append(i)
        return result