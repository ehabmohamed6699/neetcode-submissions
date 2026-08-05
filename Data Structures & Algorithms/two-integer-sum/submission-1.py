class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in pairs.keys():
                ans = [pairs[nums[i]], i]
                return ans
            pairs[(target - nums[i])] = i
        return ans