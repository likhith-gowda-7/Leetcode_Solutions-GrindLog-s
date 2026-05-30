class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total=0
        neg=0
        min_neg=float('inf')
        for val in matrix:
            for n in val:
                total+=abs(n)
                if(n<0):
                    neg+=1
                min_neg=min(min_neg,abs(n))
        if(neg%2==1):
            total-=(min_neg*2)
        return total

