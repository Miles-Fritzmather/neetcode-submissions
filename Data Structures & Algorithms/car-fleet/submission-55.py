import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [(position[i], speed[i], (target - position[i]) / speed[i]) for i in range(len(speed))]
        comb.sort(key=lambda a: a[0])
        print(comb)
        
        clusters = 1
        # for i in range(len(comb) - 1):
        #     # They will never hit, and thus cause a new cluster, when the quicker (q_) is in front positionally of the slower (s_) one
        #     (qPos, qVel, qTime) = comb[i]
        #     (sPos, sVel, sTime) = comb[i + 1]
        #     if qPos > sPos: clusters += 1

        slowest = comb[-1][2]
        for i in range(len(comb) - 2, -1, -1):
            print(slowest, clusters)
            if comb[i][2] > slowest:
                print("slowest so far. New ")
                slowest = comb[i][2]
                clusters += 1
        
        # for i in range(len(comb) - 2, -1, -1):
        #     print(comb, clusters, "looking at", comb[i])
        #     if comb[i][2] > comb[i + 1][2]:
        #         print("new cluster")
        #         clusters += 1
        #     elif comb[i + 1][1] - comb[i][1] != 0:
        #         time_to_catch_up = (comb[i][0] - comb[i + 1][0]) / (comb[i + 1][1] - comb[i][1])
        #         pos_at_catch_up = comb[i][1] * time_to_catch_up + comb[i][0]
        #         time_after = (target - pos_at_catch_up) / comb[i + 1][1]
        #         total_time = time_to_catch_up + time_after
        #         comb[i] = (comb[i][0], comb[i + 1][1], total_time)
        #         print("gets stuck behind", time_to_catch_up, pos_at_catch_up, time_after, total_time)

        return clusters