class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        count={}
        left=0
        maxlength = 0
        maxFreq = 0

        for right in range(n):
            # windowlength=right-left+1
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFreq=max(count.values())

            while (right-left+1)-maxFreq>k:
                count[s[left]]-=1
                maxFreq=max(count.values())
                left+=1
            
            maxlength=max(maxlength,right-left+1)
        return maxlength


