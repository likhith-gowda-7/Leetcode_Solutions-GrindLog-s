class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if(len(arr)<3):
            return False
        c=0
        for i in range(len(arr)):
            if(arr[i]%2==1):
                c+=1
            else:
                c=0
            if(c==3):
                return True
        return False

        