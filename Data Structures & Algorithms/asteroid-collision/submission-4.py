class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for a in asteroids:
            remove=False
            if a>0:
                st.append(a)
            else:
                magnitude=abs(a)
                while st and magnitude>st[-1] and st[-1]>0:
                    st.pop()
                if st and magnitude==st[-1] and st[-1]>0:
                    st.pop()
                    remove=True
                if st and magnitude<=st[-1] and st[-1]>0:
                    remove=True
                if not remove:
                    st.append(a) 
        return st