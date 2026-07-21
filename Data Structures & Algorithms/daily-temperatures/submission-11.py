class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        days = []
        for i in range(len(temperatures)):
            while len(days) > 0 and temperatures[i] > days[-1][0]:
                index = days.pop()[1]
                out[index] = i - index
            days.append((temperatures[i], i))

        return out

            


            



