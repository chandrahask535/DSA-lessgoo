class Solution:
    def divby13(self, s: str) -> bool:
        rem = 0
        for char in s:
            rem = (rem * 10 + int(char)) % 13
        return rem == 0
