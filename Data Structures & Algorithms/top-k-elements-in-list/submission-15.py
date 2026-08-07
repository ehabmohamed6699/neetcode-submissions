class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        freq = {}
        freq_group = {}
        max_freq = 1
        for num in nums:
            try:
                freq[num] += 1
                if freq[num] > max_freq:
                    max_freq = freq[num]
            except:
                freq[num] = 1
            try:
                freq_group[freq[num]].append(num)
            except:
                freq_group[freq[num]] = [num]
        ans = []
        i = max_freq
        while len(ans) < k:
            try:
                ans.extend(freq_group[i])
            except:
                ans
            ans = list(set(ans))
            i -= 1
        return ans
            

         