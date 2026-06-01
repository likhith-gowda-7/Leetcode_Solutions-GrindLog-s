class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lar_num=[str(num) for num in nums]
        lar_num.sort(key=lambda a: a * 10, reverse=True)
        if(lar_num[0]=="0"):
            return "0"
        return "".join(lar_num)
        