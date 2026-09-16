class Solution:
    def countSubstrings(self, s: str) -> int:
        # result=""
        def expand(l,r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            return count
        total=0
        for i in range(len(s)):
            count_even=expand(i,i+1)
            count_odd=expand(i,i)
            total+=count_even+count_odd
        return total