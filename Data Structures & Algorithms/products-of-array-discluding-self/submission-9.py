class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(1,len(nums)):
            prefix.append(nums[i - 1] * prefix[-1])
            suffix.append(nums[-(i)] * suffix[-1])

        return [prefix[i] * suffix[-(i + 1)] for i in range(len(nums))]