class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1 or len(s)==0:
            return len(s)
        left=0
        maxLen=float('-inf')
        lastSeen={} #latest index a character appears at
        for right in range(len(s)):
            if s[right] in lastSeen and lastSeen[s[right]]>=left:
                left=lastSeen[s[right]]+1
            lastSeen[s[right]]=right
            maxLen=max(maxLen, right-left+1)
        return maxLen