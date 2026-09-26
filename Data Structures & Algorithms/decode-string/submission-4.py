class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch=="]":
                word=""
                digit=""
                while st and st[-1]!="[":
                    word=st[-1]+word
                    st.pop()
                st.pop()
                while st and not st[-1].isalpha() and st[-1]!="[":
                    digit= st[-1]+digit
                    st.pop()
                digit=int(digit)
                st.append(word*digit)
            else:
                st.append(ch)
        return "".join(st)