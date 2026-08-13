class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 2}

        def internal(n):
            if n in cache: return cache[n]

            cache[n] = internal(n - 1) + internal(n - 2)
            print(n, cache[n], cache)
            return cache[n]

        return internal(n)