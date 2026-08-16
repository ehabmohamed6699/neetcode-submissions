class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        area, largest = 0, 0
        while j > i:
            area = (j - i) * min(heights[i], heights[j])
            if area > largest:
                largest = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return largest