class Solution:

    def encode(self, strs: List[str]) -> str:
        l=[]
        for st in strs:
            n=len(st)
            l.append(str(n))
            l.append("#")
            l.append(st)
        
        return "".join(l)

    #.     2#hi2#yo

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            h=s.find("#",i)
            number=int(s[i:h])
            l.append(s[h+1: h+1+number])
            i=h+1+number
        return l