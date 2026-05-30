class Solution:
    def smallestNumber(self, n: int) -> int:
        binary=bin(n)[2:]
        s="1"*len(binary)
        return int(s,2)
