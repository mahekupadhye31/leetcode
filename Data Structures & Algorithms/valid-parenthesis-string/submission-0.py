class Solution:
    def checkValidString(self, s: str) -> bool:
        #min no of open brackets (, max no of open brackets
        leftmin=0
        leftmax=0
        for ch in s:
            if leftmax<0:
                return False
            if ch=="(":
                leftmin+=1
                leftmax+=1
            elif ch==")":
                if leftmin>0:
                    leftmin-=1
                else:
                    leftmin=0
                leftmax-=1
            else:
                if leftmin>0:
                    leftmin-=1
                else:
                    leftmin=0
                leftmax+=1
        
        return leftmin==0