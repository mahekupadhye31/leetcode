from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        have=0 #no of characters (unique) we need to match 't'
        window={}
        needCount=len(need) #no of unique characters in n't'
        left=0
        bestlen=float('inf')
        bestleft,bestright=0,0
        for right in range(len(s)):
            window[s[right]]=1+window.get(s[right],0)
            if s[right] in need and need[s[right]]==window[s[right]]:
                have+=1 #one character requirement fulfilled
            
            while have==needCount:
                #wow note down this new length we have found where the requirement is satisfied
                if bestlen>right-left+1:
                    bestlen=right-left+1
                    bestleft,bestright=left,right
                #lets check if theres a smaller string possible tho
                # left+=1
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        return s[bestleft:bestright+1] if bestlen!=float('inf') else ""
            


            

        