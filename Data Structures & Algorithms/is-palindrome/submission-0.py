class Solution:
    def isPalindrome(self, s: str) -> str:
        r=""
        for c in s:
            if c.isalnum():
                r+=c.lower()
        left=0
        right=len(r)-1
        while left<right:
            if r[left]!=r[right]:
                return False
            left+=1
            right-=1    
        return True            
