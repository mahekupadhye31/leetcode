class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        count=defaultdict(int)
        left=0
        right=0
        found=0
        minLen=float("inf")
        startIndex=-1

        for ch in t:
            count[ch]+=1
        
        while right<n:
            if count[s[right]]>0:
                found+=1
            count[s[right]]-=1

            while found==m:
                if right-left+1<minLen:
                    startIndex=left
                minLen=min(minLen,right-left+1)
                count[s[left]]+=1
                if count[s[left]]>0:
                    found-=1
                left+=1
            
            right+=1
        
        return s[startIndex: startIndex+minLen] if startIndex!=-1 else ""
