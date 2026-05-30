class Solution:
    def bitwiseComplement(self, n: int) -> int:
        curr=""
        binary=bin(n)[2:]
        for b in binary:
            if(b=="1"):
                curr+="0"
            else:
                curr+="1"
        return int(curr,2)