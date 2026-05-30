class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            curr="".join(sorted(i))
            res[curr].append(i)
        return list(res.values())
        