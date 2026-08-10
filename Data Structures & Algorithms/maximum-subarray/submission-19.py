class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            if arr[i - 1] < 0: arr[i] = nums[i]
            else: arr[i] = arr[i - 1] + nums[i]

        print(arr)
        
        return max(arr)
        
        # best = nums[0]
        # curr = 0
        # i = 0
        # while i in range(len(nums)):
        #     num = nums[i]
        #     if num > 0: curr += num
        #     else:
        #         if num + curr < 0: 
        #             if i == len(nums) - 1: curr = nums[i]
        #             else: curr = nums[i + 1]
        #             best = max(best, curr)
        #             i += 2
        #             continue
        #         else: curr += num
        #     best = max(best, curr)
        #     i += 1
        # return best
            
        
        



        