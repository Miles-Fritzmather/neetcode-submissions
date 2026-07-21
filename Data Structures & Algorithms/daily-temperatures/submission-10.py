class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        days = []
        for i in range(len(temperatures)):
            while len(days) > 0 and temperatures[i] > days[-1][0]:
                val = days.pop()
                out[val[1]] = i - val[1]
            days.append((temperatures[i], i))

        return out

            


            



