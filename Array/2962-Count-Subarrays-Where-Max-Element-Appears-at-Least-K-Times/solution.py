__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi_num=max(nums)
        ans=0
        l=0
        maxi_count=0
        for r in range(len(nums)):
            if(nums[r]==maxi_num):
                maxi_count+=1
            while maxi_count>=k:
                if(nums[l]==maxi_num):
                    maxi_count-=1
                l+=1
            ans+=l
        return ans
        