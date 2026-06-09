class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        great_equ=deque()
        for val in nums:
            if(val<pivot):
                less.append(val)
            elif(val==pivot):
                great_equ.appendleft(val)
            else:
                great_equ.append(val)
        less.extend(great_equ)
        return less