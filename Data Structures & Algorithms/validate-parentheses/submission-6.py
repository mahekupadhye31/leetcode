class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if not s:
            return False

        valid={"}":"{", "]":"[",")":"("}

        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                st.append(ch)
            elif st and (ch==")" or ch=="}" or ch=="]"):
                if st[-1]!=valid[ch]:
                    return False
                st.pop()
            elif not st and (ch==")" or ch=="}" or ch=="]"):
                return False
        
        return len(st)==0
        