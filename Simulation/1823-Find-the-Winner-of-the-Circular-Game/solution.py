class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle=[]
        for i in range(1,n+1):
            circle.append(i)
        ele=0
        k-=1
        while len(circle)>1:
            ele=(ele+k)%len(circle)
            circle.pop(ele)
        return circle[0]
        