class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        m=len(s1)
        n=len(s2)
        c=Counter(s1)
        count={}

        for i in range(n):
            count[s2[i]]=1+count.get(s2[i],0)
            if i-left+1>m:
                count[s2[left]]-=1
                if count[s2[left]]==0:
                    del count[s2[left]]
                left+=1
            if count==c:
                return True
        return False