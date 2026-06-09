class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        order = []
        for num in counts:
            order.append((num, counts[num]))
        order.sort(key=sorter)
        final = [o[0] for o in order]

        return final[-k:]
    
def sorter(pair):
    return pair[1]
            

            
        