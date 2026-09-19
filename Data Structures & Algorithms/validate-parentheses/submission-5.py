class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if not s:
            return False
        valid={"}":"{", "]":"[",")":"("}
        for b in s:
            if b=="(" or b=="[" or b=="{":
                st.append(b)
            elif st and (b=="}" or b==")" or b=="]"):
                if st[-1]!=valid[b]:
                    return False
                st.pop()
            elif not st and (b=="}" or b==")" or b=="]"):
                return False
            
        return True if len(st)==0 else False