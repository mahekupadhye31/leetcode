class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordSet=set(wordDict)
        dp=[-1]*n

        def f(i):
            if i>n-1:
                return True
                
            #in case we have already computed this subproblem before
            if dp[i]!=-1:
                return dp[i]
            temp=""
            for j in range(i,n):
                temp+=s[j]
                if temp in wordSet and f(j+1):
                    dp[i]=True
                    return True
            
            dp[i]=False
            return False
        
        return f(0)