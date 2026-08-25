class Solution:
    def isPalindrome(self, s: str) -> bool:
        front=""
        back=""
        for ch in s.lower():
            if ch.isalnum():
                front=front+ch
        for ch in reversed(s.lower()):
            if ch.isalnum():
                back=back+ch
        return front==back