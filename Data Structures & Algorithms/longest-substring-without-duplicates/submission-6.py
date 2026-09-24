class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index={}
        left=0
        right=0
        n=len(s)
        maxLen=float("-inf")
        if len(s)==0:
            return 0
        for right in range(n):
            if s[right] not in index:
                index[s[right]]=right
                maxLen=max(maxLen, right-left+1)
            else:
                left=max(left,index[s[right]]+1) #left shouldnt move backwards
                index[s[right]]=right #stores the most recent index
                maxLen=max(maxLen, right-left+ 1)
        
        return maxLen
