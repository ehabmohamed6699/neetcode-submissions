class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        for c in t:
            if c in freq:
                freq[c] -= 1
            else:
                return False
        for i in freq.values():
            if i != 0:
                return False
        return True