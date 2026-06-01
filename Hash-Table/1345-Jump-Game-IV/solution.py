class Solution:
    def minJumps(self, arr: List[int]) -> int:
        h1=defaultdict(list)
        for i,val in enumerate(arr):
            h1[val].append(i)
        n=len(arr)
        if(n==1):
            return 0
        q=deque([(0,0)])
        seen=[0]*n
        seen[0]=1
        while q:
            idx,jump=q.popleft()
            if((idx+1)<n and seen[idx+1]!=1):
                if((idx+1)==n-1):
                    return jump+1
                q.append((idx+1,jump+1))
                seen[idx+1]=1
            if((idx-1)>0 and seen[idx-1]!=1):
                q.append((idx-1,jump+1))
                seen[idx-1]=1
            while h1[arr[idx]]:
                i=h1[arr[idx]].pop()
                if(i==n-1):
                    return jump+1
                elif(seen[i]!=1):
                    q.append((i,jump+1))
                    seen[i]=1