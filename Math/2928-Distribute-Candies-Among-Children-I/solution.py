class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        mini=min(n,limit)
        count=0
        for i in range(mini+1):
            for j in range(mini+1):
                z=n-(i+j)
                if(z>=0 and z<=limit and (i+j+z)==n):
                    count+=1
        return count