class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        after = [1] * len(nums)

        for i in range(0, len(nums) - 1):
            before[i + 1] = before[i] * nums[i]
        
        for i in range(len(nums) - 1, 0, -1):
            after[i - 1] = after[i] * nums[i]


        #  0  1 2 3
        # 48 24 6 1


        print(before)
        print(after)
        res = [before[i] * after[i] for i in range(len(nums))]
        return res