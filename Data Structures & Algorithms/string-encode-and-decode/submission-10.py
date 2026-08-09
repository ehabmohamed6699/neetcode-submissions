class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "&::&"
        if len(strs) == 1 and strs[0] == "":
            return strs[0]
        new_strs = ["<emp>" if s == "" else s for s in strs]
        print(new_strs)
        return "&::&".join(new_strs)
    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "&::&":
            return []
        strs = ["" if st == "<emp>" else st for st in s.split("&::&")]
        return strs