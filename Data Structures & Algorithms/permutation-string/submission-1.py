from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count=Counter(s1)
        newCount=Counter(s2[0:len(s1)])
        if count==newCount:
            return True
        for left in range(1,len(s2)-len(s1)+1):
            newCount[s2[left+len(s1)-1]]=1+newCount[s2[left+len(s1)-1]]
            newCount[s2[left-1]]-=1
            if newCount==count:
                return True
        return False
            

