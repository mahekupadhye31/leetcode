class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs[0])
        i=0
        while i<n:
            for j in range(1,len(strs)):
                if i<len(strs[j]):
                    if strs[0][i]!=strs[j][i]:
                        return strs[0][0:i] 
                else:
                    return strs[0][0:i]
            i+=1
        return strs[0]