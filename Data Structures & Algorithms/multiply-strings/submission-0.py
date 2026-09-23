class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m=len(num1)
        n=len(num2)

        result=[0]*(m+n) 

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                a=int(num1[i])
                b=int(num2[j])
                result[i+j+1]=result[i+j+1]+a*b
                result[i+j]+=result[i+j+1]//10
                result[i+j+1]=(result[i+j+1])%10
        
        while i<m+n and result[i]==0:
            i+=1

        if i==m+n:
            return "0"

        return "".join(str(digit) for digit in result[i:])