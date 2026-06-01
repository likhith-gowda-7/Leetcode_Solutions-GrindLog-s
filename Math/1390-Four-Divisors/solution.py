class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def find(num,d):
            c=0
            curr=0
            for i in range(1,d+1):
                rem=num%i
                if(rem==0):
                    c+=1
                    curr+=i
                    diff=num//i
                    curr+=diff
                    if(diff!=i and diff<=num):
                        c+=1
                if(c>4):
                    return 0
            return curr if(c==4) else 0
        res=0
        for val in nums:
            s=math.floor(math.sqrt(val))
            res+=find(val,s)
        return res