class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        h1 = defaultdict(list)
        for i, val in enumerate(nums):
            h1[val].append(i)
        res = float("inf")
        for key, val in h1.items():
            l = len(val)
            if l > 2:
                for a in range(l):
                    i = val[a - 2]
                    j = val[a - 1]
                    k = val[a]
                    x = abs(i - j) + abs(j - k) + abs(k - i)
                    res = min(res, x)
        return res if (res != float("inf")) else -1