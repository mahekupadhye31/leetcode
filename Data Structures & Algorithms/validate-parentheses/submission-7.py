class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        if not s:
            return False

        valid={"}":"{", "]":"[",")":"("}

        for ch in s:
            if ch=="(" or ch=="{" or ch=="[":
                st.append(ch)
            elif ch==")" or ch=="}" or ch=="]":
                if len(st)==0:
                    return False
                if st[-1]!=valid[ch]:
                    return False
                st.pop()
        return len(st)==0    