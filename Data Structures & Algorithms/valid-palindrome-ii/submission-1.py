class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                remleft=isPalindrome(left+1,right)
                remright=isPalindrome(left,right-1)
                if not (remleft or remright):
                    return False
            left+=1
            right-=1
        return True