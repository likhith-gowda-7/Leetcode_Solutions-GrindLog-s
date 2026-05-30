class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n=len(arr)
        memo={}
        def dfs(idx):
            if(idx in memo):
                return memo[idx]
            curr=0
            for jump in range(1,d+1):
                left=(idx-jump)
                if(0<=left<n and arr[idx]>arr[left]):
                    curr=max(curr,dfs(left))
                else:
                    break
            for jump in range(1,d+1):
                right=(idx+jump)
                if(0<=right<n and arr[idx]>arr[right]):
                    curr=max(curr,dfs(right))
                else:
                    break
            memo[idx]=1+curr
            return memo[idx]
        res=0
        for i in range(n):
            res=max(res,dfs(i))
        return res