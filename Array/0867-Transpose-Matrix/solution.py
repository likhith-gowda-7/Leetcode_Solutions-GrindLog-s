class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in zip(*matrix):
            res.append(i)
        return res