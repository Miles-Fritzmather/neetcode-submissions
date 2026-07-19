class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i, n in enumerate(nums):
            vals = self.twoSum(-n, nums[i + 1:])
            for val in vals:
                res.add((n, val[0], val[1]))

        return list(res)

    def twoSum(self, target: int, nums: List[int]) -> List[(int, int)]:
        results = []
        vals = set()
        for n in nums:
            if target - n in vals: results.append((target - n, n))
            vals.add(n)

        # print(nums, target, results)
        return results