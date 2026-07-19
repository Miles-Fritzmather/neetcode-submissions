class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        biggest = numbers[-1]
        l = 0
        while numbers[l] < target - biggest and l < len(numbers) - 1:
            l += 1

        r = l + 1
        while numbers[l] + numbers[r] != target:
            r += 1
            if r == len(numbers):
                l += 1
                r = l + 1

        return [l + 1, r + 1]