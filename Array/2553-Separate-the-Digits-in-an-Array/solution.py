class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def rev(num):
            curr=deque()
            while num:
                last=num%10
                curr.appendleft(last)
                num//=10
            nonlocal res
            res.extend(curr)
        res=[]
        for num in nums:
            rev(num)
        return res