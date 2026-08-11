class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            try:
                freq[num] += 1
            except:
                freq[num] = 1
        keys = list(freq.keys())
        high, highest = 0, 0
        origin, current = 0, 0
        while len(keys) > 0:
            origin = keys[0]
            current = origin
            del freq[current]
            high = 1
            while True:
                current = current - 1
                try:
                    del freq[current]
                    high += 1
                except:
                    break
            current = origin
            while True:
                current = current + 1
                try:
                    del freq[current]
                    high += 1
                except:
                    break
            if high > highest:
                highest = high
            keys = list(freq.keys())
        return highest