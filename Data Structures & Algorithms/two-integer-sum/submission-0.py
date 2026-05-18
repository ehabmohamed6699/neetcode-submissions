class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i in range(len(nums)):
            if target - nums[i] in s:
                return [s[target - nums[i]],i]
            elif nums[i] not in s:
                s[nums[i]] = i
            else:
                continue