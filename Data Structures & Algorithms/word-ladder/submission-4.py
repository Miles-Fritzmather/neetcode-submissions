class Solution:
    def ladderLength(self, beginWord: str, goal: str, wordList: List[str]) -> int:
        def oneAway(a: str, b:str) -> bool:
            missed = False
            for i in range(len(a)):
                if (a[i] != b[i]):
                    if missed: return False
                    missed = True
            return True

        # options = [opt for opt in wordList if oneAway(opt, word) and opt not in path]
        options = [(beginWord, [beginWord])]
        while options:
            word, path = options.pop()
            print(word, path, "|", options)
            if word == goal: 
                print("FOUND IT")
                return len(path)
            for option in wordList:
                if oneAway(option, word) and option not in path:
                    if option == goal: return len(path) + 1
                    options.append((option, path + [option]))

            # best = min(internal(opt, path), best)
            # path.pop()

        return 0

        # res = internal(beginWord, [])
        # return res if res != float('inf') else 0
