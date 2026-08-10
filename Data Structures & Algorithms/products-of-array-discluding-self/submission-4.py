class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total_without_zeros = 1
        total_zeros = 0
        for num in nums:
            total *= num
            if num != 0:
                total_without_zeros *= num
            else:
                total_zeros += 1
        return [total // n if n != 0 else total_without_zeros if total_zeros == 1 else total for n in nums]