class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def cind(char):
            return ord(char.lower()) - ord('a') 
        
        matches = 0
        ALPHABET = 26

        if len(s1) > len(s2): return False
        
        s1Counts, s2Counts = [0] * ALPHABET, [0] * ALPHABET
        
        for i in range(0, len(s1)): 
            s1Counts[cind(s1[i])] += 1
            s2Counts[cind(s2[i])] += 1
        
        matches = sum([1 if s1Counts[i] == s2Counts[i] else 0 for i in range(0, ALPHABET)])
        print(matches)
        for i in range(0, len(s2) - len(s1)):
            if matches == ALPHABET: return True

            losing, adding = cind(s2[i]), cind(s2[i + len(s1)])

            s2Counts[adding] += 1
            if s1Counts[adding] == s2Counts[adding]:
                matches += 1
                print("found end match:", s2[i + len(s1)], i, matches, s2Counts)
            elif s2Counts[adding] == s1Counts[adding] + 1:
                matches -= 1
                print("lost end match:", s2[i + len(s1)], i, matches, s2Counts)

            prev = s2Counts[losing]
            s2Counts[losing] = max(0, s2Counts[losing] - 1)
            if prev == s2Counts[losing]: continue
            if s2Counts[losing] == s1Counts[losing]:
                matches += 1
                print("found start match:", s2[i], i, matches, s2Counts)
            elif s2Counts[losing] == s1Counts[losing] - 1:
                matches -= 1
                print("lost start match:", s2[i], i, matches, s2Counts)
                

            # print(matches, s2[i], s2[i + len(s1)], counts)
        return matches == ALPHABET





# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         def cind(char):
#             return ord(char.lower()) - ord('a') 
        
        
#         if len(s1) > len(s2): return False
        
#         small_counts = [0] * 26
#         for c in s1: small_counts[cind(c)] += 1
        
#         counts = [0] * 26
#         for i in range(0, len(s1)): counts[cind(s2[i])] += 1
#         if counts == small_counts: return True

#         for i in range(0, len(s2) - len(s1)):
#             counts[cind(s2[i])] = max(0, counts[cind(s2[i])] - 1)
#             counts[cind(s2[i + len(s1)])] += 1
#             if counts == small_counts: return True
        

#         return False