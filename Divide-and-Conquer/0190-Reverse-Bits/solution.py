class Solution:
    def reverseBits(self, n: int) -> int:
        binary=bin(n)[2:][::-1]
        l=len(binary)
        for _ in range(l,32):
            binary+="0"
        return int(binary,2)