class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            even=expand(i,i+1)
            odd=expand(i,i)
            if len(even)>len(result):
                result=even
            if len(odd)>len(result):
                result=odd
        return result