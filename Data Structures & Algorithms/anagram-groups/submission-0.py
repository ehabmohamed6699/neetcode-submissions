class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            try:
                groups[key].append(s)
            except:
                groups[key] = [s]
        return list(groups.values())