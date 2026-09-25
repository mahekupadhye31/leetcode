class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if st and t=="+":
                first=st.pop()
                second=st.pop()
                st.append(first+second)
            elif st and t=="*":
                first=st.pop()
                second=st.pop()
                st.append(first*second)
            elif st and t=="-":
                first=st.pop()
                second=st.pop()
                st.append(second-first)
            elif st and t=="/":
                first=st.pop()
                second=st.pop()
                st.append(int(second/first))
            else:
                st.append(int(t))
        return st[-1]