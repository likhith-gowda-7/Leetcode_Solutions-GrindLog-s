class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        check=Counter(tiles)
        def backtrack():
            res=0
            for c in check:
                if(check[c]>0):
                    check[c]-=1
                    res+=1
                    res+=backtrack()
                    check[c]+=1
            return res
        return backtrack()