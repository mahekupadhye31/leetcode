class Solution:

    def encode(self, strs: List[str]) -> str:
        t=""
        for s in strs:
            t = t+ (str(len(s))+"#"+s)
        return t
        # t= 5#hello5#world

    def decode(self, s: str) -> List[str]:
        res=[]
        i,n=0,len(s)
        while i<n:
            j=s.find('#',i)
            digit= int(s[i:j])
            substring=s[j+1:j+1+digit]
            i=j+1+digit
            res.append(substring)
        return res