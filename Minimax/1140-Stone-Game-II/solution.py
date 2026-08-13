class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]

        @cache
        def dfs(i, M):
            if i + M * 2 >= n:
                return piles[i]
            res=float('inf')
            for x in range(1,2*M+1):
                res=min(res,dfs(i+x,max(M,x)))
            return piles[i]-res
        return dfs(0, 1)