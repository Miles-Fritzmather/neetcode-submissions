class Solution:
    def ladderLength(self, beginWord: str, goal: str, wordList: List[str]) -> int:
        def oneAway(a: str, b:str) -> bool:
            missed = False
            for i in range(len(a)):
                if (a[i] != b[i]):
                    if missed: return False
                    missed = True
            return True

        options = [(beginWord, [beginWord])]
        while options:
            word, path = options.pop()
            for option in wordList:
                if oneAway(option, word) and option not in path:
                    if option == goal: return len(path) + 1
                    options.append((option, path + [option]))

        return 0