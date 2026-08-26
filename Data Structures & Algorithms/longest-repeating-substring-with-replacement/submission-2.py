class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        count={}
        m=float('-inf')
        maxFreq=float('-inf')
        while right<len(s):
            length=right-left+1
            count[s[right]]=1+count.get(s[right],0)
            maxFreq=max(maxFreq,count[s[right]])
            if length-maxFreq<=k:
                m=max(m,right-left+1)
                right+=1
            else:
                if count[s[left]]:
                    count[s[left]]=count[s[left]]-1
                left+=1
                right+=1
        return m