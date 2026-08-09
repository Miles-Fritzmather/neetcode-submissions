class Solution:
    def ladderLength(self, beginWord: str, goal: str, wordList: List[str]) -> int:
        def oneAway(a: str, b:str) -> bool:
            missed = False
            for i in range(len(a)):
                if (a[i] != b[i]):
                    if missed: return False
                    missed = True
            return True

        options = deque([(beginWord, 1)])
        path = set([beginWord])
        while options:
            word, count = options.popleft()
            for option in wordList:
                if oneAway(option, word) and option not in path:
                    if option == goal: return count + 1
                    path.add(option)
                    options.append((option, count + 1))

        return 0