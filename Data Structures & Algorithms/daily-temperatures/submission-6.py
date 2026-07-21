class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0 for t in temperatures]
        days = []
        j = 0
        for i in range(len(temperatures)):
            while len(days) > 0 and temperatures[i] > days[-1][0]:
                val = days.pop()
                out[val[1]] = i - val[1]
        
            frame = (temperatures[i], i)
            print("adding to stack", frame)
            days.append(frame)

        return out

            


            



