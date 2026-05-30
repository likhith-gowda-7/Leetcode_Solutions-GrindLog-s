class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #here the idea(main core) is to find the subset with sum with half of the total sum of the array
        target=sum(nums)
        #Base case if the total sum itself is odd, then you can't make two subset of equal sum...
        if(target%2):
            return False
        target//=2
        #Modified Memoiazation (Top-Down)
        #this dp set holds the sub_set numbers that have been formed
        dp=set()
        dp.add(0)
        for num in nums:
            '''this curr_dp holds all the previously found sub_set numbers(dp_set)
            And
            the new sub_numbers that can be formed using current number by adding the prev sub_set numbers + current number...
            ''' 
            curr_dp=dp.copy()
            for sub_num in dp:
                new_subset_num=num+sub_num
                if(new_subset_num==target):
                    return True
                curr_dp.add(new_subset_num)
                #Optimiazation Trick (Early return)
            #After all that, we make curr_dp as actual dp. becoz it consists all the subset numbers till the current number!!!
            dp=curr_dp
        return False

            
        

        