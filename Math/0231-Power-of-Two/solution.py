class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binary=bin(n)
        return n>0 and binary.count("1")==1