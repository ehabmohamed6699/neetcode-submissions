class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_1, freq_2 = [0]*26, [0]*26
        for c in s:
            freq_1[ord(c) - 97] += 1
        for c in t:
            freq_2[ord(c) - 97] += 1
        if freq_1 == freq_2:
            return True
        return False