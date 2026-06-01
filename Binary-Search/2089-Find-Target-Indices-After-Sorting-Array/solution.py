class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less=0
        dup=0
        for i in nums:
            if(i<target):
                less+=1
            elif(i==target):
                dup+=1
        l=[]
        for j in range(less,less+dup):
            l.append(j)
        return l
        

        