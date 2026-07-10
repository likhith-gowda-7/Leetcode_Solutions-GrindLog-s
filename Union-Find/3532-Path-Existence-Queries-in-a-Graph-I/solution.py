class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent=[-1]*n
        for i in range(1,n):
            if(abs(nums[i]-nums[i-1])<=maxDiff):
                parent[i]=parent[i-1]
            else:
                parent[i]=i
        res=[]
        for u,v in queries:
            path=False
            if(parent[u]==parent[v]):
                path=True
            res.append(path)
        return res