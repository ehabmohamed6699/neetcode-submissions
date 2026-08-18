class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        long, longest = 1,1
        cur_idx = 0
        freq = {s[cur_idx]: 1}
        i = 1
        while i < len(s):
            try:
                freq[s[i]] += 1
                freq[s[cur_idx]] -= 1
                if freq[s[cur_idx]] == 0:
                    del freq[s[cur_idx]]
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                cur_idx += 1
                i -= 1
            except:
                freq[s[i]] = 1
            long = (i - cur_idx) + 1
            if long > longest:
                longest = long
            i += 1
        return longest