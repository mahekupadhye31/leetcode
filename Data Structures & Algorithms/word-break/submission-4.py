class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        n=len(s)
        dp=[-1]*n

        def f(i):
            if i>n-1:
                return True
            
            if dp[i]!=-1:
                return dp[i]

            temp=""

            for j in range(i,n):
                temp+=s[j]
                if temp in wordset and f(j+1):
                    dp[j]=True
                    return True
            
            dp[i]=False
            return False
        
        return f(0)