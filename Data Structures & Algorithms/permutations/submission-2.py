class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        if len(nums) == 0: return [[]]
        if len(nums) == 1: return [nums]

        perms = self.permute(nums[1:])
        print("perms:", perms)
        res = []

        for perm in perms:
            print(perm)
            for i in range(len(perm) + 1):
                res.append(perm[0:i] + [nums[0]] + perm[i:])
            print(res)

        return res


    
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     perms = [[n] for n in nums]

    #     def increment(current: List[List[int]]):
    #         new = []
    #         for perm in current:
    #             for num in nums:
    #                 if num in perm: continue
    #                 new.append(perm + [num])
    #         return new


    #     for i in range(1, len(nums)):
    #         perms = increment(perms)

    #     return perms