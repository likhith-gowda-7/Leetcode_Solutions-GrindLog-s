class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(1,n-1):
            #this condition ensures that the current val is unique and left always contains genuine neighbour(left!=curr_val)
            if(nums[i]==nums[i-1]):
                continue
            curr_val=nums[i]
            left=nums[i-1]
            right=i+1
            #this condition skips the duplicates at right side of the current value and points at the right neighbour(right!=curr_val)
            while right<n and nums[right]==curr_val:
                right+=1
            if(right<n):
                #this condition checks if current value is a "Hill" or a "Valley"?
                if((left<curr_val and curr_val>nums[right]) or (left>curr_val and curr_val<nums[right])):
                    count+=1
        return count