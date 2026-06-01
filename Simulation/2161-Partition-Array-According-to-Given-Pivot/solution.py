class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        great=[]
        c=0
        for i in nums:
            if(i<pivot):
                less.append(i)
            elif(i>pivot):
                great.append(i)
            else:
                c+=1
        res=[]
        res+=less
        res+=[pivot]*c
        res+=great
        return res