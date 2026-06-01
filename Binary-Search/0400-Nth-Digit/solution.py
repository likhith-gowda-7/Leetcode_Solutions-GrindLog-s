class Solution:
    def findNthDigit(self, n: int) -> int:
        if(n<10):
            return n
        else:
            d = 1  # Number of digits in the current group
            count = 9  # Total numbers in the group
            num = n  
            while num > d * count:  
                num -= d * count  # Subtract the digits covered in this group
                d += 1  # Move to the next digit group
                count *= 10  # Next group has 10 times more numbers
            
            group_ind=num-1
            start_ind=10**(d-1)
            target=start_ind+(group_ind//d)
            res_ind=group_ind%d
            res=str(target)
            return int(res[res_ind])