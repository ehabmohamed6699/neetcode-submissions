class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        freq = {}
        for num in nums:
            try:
                freq[num] += 1
            except:
                freq[num] = 1
        buckets = [[] for i in range(len(nums) + 1)]
        for key, val in freq.items():
            buckets[val].append(key)
        ans = []
        i = len(nums)
        while len(ans) < k:
            try:
                ans.extend(buckets[i])
            except:
                ans
            i -= 1
        return ans
            

         