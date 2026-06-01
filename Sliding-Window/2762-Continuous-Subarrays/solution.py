class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l=0
        maxi=deque()
        mini=deque()
        c=0
        for r in range(len(nums)):
            while maxi and nums[maxi[-1]]<=nums[r]:
                maxi.pop()
            while mini and nums[mini[-1]]>=nums[r]:
                mini.pop()
            maxi.append(r)
            mini.append(r)
            while nums[maxi[0]]-nums[mini[0]]>2:
                l+=1
                if(maxi[0]<l):
                    maxi.popleft()
                if(mini[0]<l):
                    mini.popleft()
            c+=r-l+1   
        return c             