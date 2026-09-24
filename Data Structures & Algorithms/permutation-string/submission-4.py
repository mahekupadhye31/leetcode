class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)
        count=Counter(s1)
        window=defaultdict(int)
        left=0

        for right in range(n):
            window[s2[right]]+=1
            if right-left+1>m:
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            
            if window==count:
                return True
        
        return False