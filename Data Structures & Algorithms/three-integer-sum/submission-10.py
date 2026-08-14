class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        elif len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -nums[i]
            j, k = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while k > j:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[j] + nums[k] < target:
                    j += 1
                if nums[j] + nums[k] > target:
                    k -= 1
                
        return result

        