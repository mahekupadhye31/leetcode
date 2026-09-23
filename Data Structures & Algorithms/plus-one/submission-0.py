class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        carry=0

        for i in range(n-1,-1,-1):
            if i==n-1:
                value=digits[i]+carry+1
                digits[i]=value%10
            else:
                value=digits[i]+carry
                digits[i]=value%10
            carry=value//10
        
        if carry:
            digits.insert(0,carry)
        return digits
            
        