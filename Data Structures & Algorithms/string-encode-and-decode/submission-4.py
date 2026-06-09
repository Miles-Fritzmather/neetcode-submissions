class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "{{N/A}}"
        
        print("|||||".join(strs))
        return "|||||".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "{{N/A}}": return []
        
        print(s.split("|||||"))
        return s.split("|||||")
