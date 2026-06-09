class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for n, c in counts.items():
            freq[c].append(n)
            
        res = []
        print(freq)
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
            
            
        # order = []
        # for num in counts:
        #     order.append((num, counts[num]))
        # order.sort(key=sorter)
        # final = [o[0] for o in order]

        # return final[-k:]
    
# def sorter(pair):
#     return pair[1]