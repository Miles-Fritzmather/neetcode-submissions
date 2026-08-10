class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = 0
        i = 0
        while i in range(len(nums)):
            num = nums[i]
            # print("new #:", num, "| curr:", curr, "best:", best)
            if num > 0: 
                # print("adding")
                curr += num
            else:
                if num + curr < 0: 
                    # print("bad")
                    if i == len(nums) - 1:  
                        curr = nums[i]
                    else:
                        curr = nums[i + 1]
                    best = max(best, curr)
                    i += 2
                    continue
                else: 
                    # print("adding2")
                    curr += num
            best = max(best, curr)
            i += 1
        # for num in nums:
        #     if num > 0: curr += num
        #     else:
        #         if num + curr < 0: curr = num
        #         else: curr += num
        #     best = max(best, curr)
        #     print(curr, best)
        return best
            
        
        
        # left = [nums[0]] * len(nums)
        # for i in range(1, len(nums)): left[i] = left[i - 1] + nums[i]
        # right = [nums[-1]] * len(nums)
        # for i in range(len(nums) - 2, -1, -1): right[i] = right[i + 1] + nums[i]

        # print(left, right)

        # best_l = 0
        # best_r = 0
        # for i in range(len(nums)):
        #     if left[i] > left[best_l]: best_l = i
        #     if right[i] > right[best_r]: best_r = i

        # print(best_l, best_r)
        
        # return sum(nums[best_r:best_l + 1])