class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result=result+str(len(s))+"#"+s
        return result

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            length=int(s[i:j])
            string=s[j+1:j+1+length]
            ans.append(string)
            i=j+1+length
        return ans
