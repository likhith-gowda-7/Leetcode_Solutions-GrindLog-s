class Solution:
    def kthCharacter(self, k: int) -> str:
        count=bin(k-1).count("1")   #this is used to count no. of 1's in number's binary rep
        return chr(97+count)