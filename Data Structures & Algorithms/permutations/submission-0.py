class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[n] for n in nums]

        def increment(current: List[List[int]]):
            new = []
            for perm in current:
                for num in nums:
                    if num in perm: continue
                    new.append(perm + [num])
            return new


        for i in range(1, len(nums)):
            perms = increment(perms)

        return perms