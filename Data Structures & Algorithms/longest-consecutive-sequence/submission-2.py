class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        high, highest = 0, 0
        origin, current = 0, 0
        while len(elements) > 0:
            origin = elements.pop()
            current = origin
            high = 1
            while True:
                current = current - 1
                try:
                    elements.remove(current)
                    high += 1
                except:
                    break
            current = origin
            while True:
                current = current + 1
                try:
                    elements.remove(current)
                    high += 1
                except:
                    break
            if high > highest:
                highest = high
        return highest