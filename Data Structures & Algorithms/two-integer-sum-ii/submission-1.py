class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            diff = target - numbers[i]
            if diff == numbers[j]:
                return [i+1, j+1]
            elif diff > numbers[j]:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]