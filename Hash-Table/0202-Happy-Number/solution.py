class Solution:
    def isHappy(self, n: int) -> bool:
        def power_of_numbers(n):
            val=0
            while n>0:
                last=n%10
                val+=last*last
                n//=10
            return val
        seen=set()
        while n!=1:
            if(n in seen):
                return False
            seen.add(n)
            n=power_of_numbers(n)
        return True