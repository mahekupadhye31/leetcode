class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=set()
        left=0
        right=0
        index={}
        maxLength=1
        if len(s)==0:
            return 0
        while right<len(s):
            if s[right] not in visited:
                visited.add(s[right])
                index[s[right]]=right
                maxLength=max(maxLength, right-left+1)
                right+=1
            else:
                left = max(left, index[s[right]] + 1)
                index[s[right]]=right
                maxLength=max(maxLength, right-left+1)
                right+=1
        return maxLength