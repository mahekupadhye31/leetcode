class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=[]
        for op in ops:
            if op=="+":
                top1=st[-1] if len(st)>0 else 0
                top2=st[-2] if len(st)>1 else 0
                st.append(int(top1)+int(top2))
            elif op=="C":
                if len(st)>0: st.pop()
            elif op=="D":
                if len(st)>0: 
                    top1=st[-1]
                    st.append(int(top1)*2)
            else:
                st.append(int(op))
        return sum(st) 
