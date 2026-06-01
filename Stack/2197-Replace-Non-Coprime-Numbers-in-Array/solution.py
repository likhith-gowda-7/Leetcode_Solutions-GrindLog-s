class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for n in nums:
            val=n
            while(stack and gcd(stack[-1],val)>1):
                prev=stack.pop()
                LCM=lcm(prev,val)
                val=LCM
            stack.append(val)
        return stack