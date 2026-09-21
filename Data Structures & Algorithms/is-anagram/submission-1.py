class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        # count={}

        # for ch in s:
        #     count[ch]=1+count.get(ch,0)
        # for ch in t:
        #     if ch in count and count[ch]!=0:
        #         count[ch]=count[ch]-1
        
        # for ch in count:
        #     if count[ch]!=0:
        #         return False
        # return True

        return sorted(s)==sorted(t)