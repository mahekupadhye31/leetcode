class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        maxLen=0
        maxFreq=0
        mpp = defaultdict(int)
        while r<len(s):
            mpp[s[r]]+=1
            maxFreq=max(maxFreq,mpp[s[r]])
            while (r-l+1)-maxFreq>k:
                mpp[s[l]]-=1
                l+=1
            if (r-l+1)-maxFreq<=k:
                maxLen=max(maxLen, (r-l+1))
            r+=1
        return maxLen        


