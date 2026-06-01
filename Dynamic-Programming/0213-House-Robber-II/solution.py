class Solution:
    def rob(self, nums: List[int]) -> int:
        #Main Tip: if you rob starting robbing from house-1,then you can't rob house-n(last house)becoz they're adjacent 
        '''So, the limit is (0-n-1)->(house1 to house(n-1)) and (1-n)->(house2 to house-n)'''
        n=len(nums)
        if(n<=2):
            return max(nums)
        def solve(arr):
            n1=arr[0]
            n2=max(arr[1],n1)
            for money in arr[2:]:
                n1,n2=n2,max(n2,money+n1)
            return n2
        return max(solve(nums[:-1]),solve(nums[1:]))
