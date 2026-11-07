class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for t in tokens:
            if t=="+":
                if len(st)>1:
                    t1=st.pop()
                    t2=st.pop()
                    st.append(int(t1)+int(t2))
            elif t=="*":
                if len(st)>1:
                    t1=st.pop()
                    t2=st.pop()
                    st.append(int(t1)*int(t2))
            elif t=="-":
                if len(st)>1:
                    t1=st.pop()
                    t2=st.pop()
                    st.append(int(t2)-int(t1))
            elif t=="/":
                if len(st)>1:
                    t1=st.pop()
                    t2=st.pop()
                    st.append(int(int(t2)/int(t1)))
            else:
                st.append(int(t))
        return st[-1]