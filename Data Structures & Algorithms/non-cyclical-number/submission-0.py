class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        new_total=0

        while True:
            for digit in str(n):
                digit = int(digit)
                new_total+=digit*digit
            n=new_total
            new_total=0
            if n in visited:
                return False
            visited.add(n)
            if n==1:
                return True

        return False