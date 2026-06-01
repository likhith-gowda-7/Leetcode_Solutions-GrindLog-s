class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #Counting Sort
        count=[0]*(3)
        #here we count the freq of each element
        for num in nums:
            count[num]+=1
        #i refers the index in nums list
        i=0
        #here we traverse the freq arr
        for j in range(3):
            #if the count[j]>0, that means that this num is present in nums and need to be added
            while count[j]>0:
                nums[i]=j
                i+=1
                count[j]-=1

        