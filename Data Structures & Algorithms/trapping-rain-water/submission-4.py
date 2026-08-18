class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        l, r = [height[0]], [height[-1]]
        for j in range(1, len(height)):
            l.append(max(l[-1], height[j]))
            r.append(max(r[-1], height[-(j+1)]))
        l, r = l[:-2], r[:-2]
        r.reverse()
        total = 0
        for j in range(len(l)):
            curr = min(l[j], r[j]) - height[j+1]
            total += max(curr, 0)
        return total