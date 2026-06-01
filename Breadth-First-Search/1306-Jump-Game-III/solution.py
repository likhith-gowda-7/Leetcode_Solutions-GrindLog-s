class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        q=deque([start])
        while q:
            idx=q.popleft()
            if(arr[idx]=="#"):
                continue
            elif(arr[idx]==0):
                return True
            val=arr[idx]
            arr[idx]="#"
            for choice in [val,-val]:
                curr=idx+choice
                if(0<=curr<n and arr[curr]!="#"):
                    q.append(curr)
        return False