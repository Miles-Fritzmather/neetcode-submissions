class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        waiting = []
        ready = []
        cycle = 0
        jobs = {}
        for task in tasks:
            jobs[task] = 1 + jobs.get(task, 0)
        
        heapq.heapify(ready)
        for job, count in jobs.items():
            heapq.heappush(ready, -count)

        while ready or waiting:
            if len(ready) != 0:
                val = heapq.heappop(ready)
                if val < -1:
                    waiting.append((val + 1, cycle + n))

            if waiting and waiting[0][1] == cycle:
                heapq.heappush(ready, waiting.pop(0)[0])

            cycle += 1
            

        return cycle