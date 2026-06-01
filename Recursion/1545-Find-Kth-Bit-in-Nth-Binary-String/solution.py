class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev="0"
        n-=1
        curr_len=1
        while n>0 and curr_len<k:
            curr=""
            for val in prev:
                if(val=="0"):
                    curr+="1"
                else:
                    curr+="0"
            prev+="1"+curr[::-1]
            curr_len=(curr_len*2)+1
            n-=1
        return prev[k-1]