class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st=[]
        pairs=list(zip(position,speed))
        pairs.sort(reverse=True)
        for p,s in pairs:
            time=(target-p)/s
            if st and time<=st[-1]:
                continue
            st.append(time)
        return len(st)