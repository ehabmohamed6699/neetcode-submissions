import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = "".join(re.findall("[a-zA-Z0-9]", s))
        x = x.lower()
        return x[::-1] == x
        