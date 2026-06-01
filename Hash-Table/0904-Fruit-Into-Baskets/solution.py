class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res=0
        bucket=defaultdict(int)
        n=len(fruits)
        l=0
        for r in range(n):
            if(fruits[r] not in bucket):
                res=max(res,(r-l))
                while len(bucket)==2:
                    bucket[fruits[l]]-=1
                    if(bucket[fruits[l]]==0):
                        del bucket[fruits[l]]
                    l+=1
            bucket[fruits[r]]+=1
        res=max(res,n-l)
        return res