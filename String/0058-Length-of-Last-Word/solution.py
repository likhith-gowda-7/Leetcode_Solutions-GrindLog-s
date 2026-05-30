class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.split()
        last_len=arr[-1]
        return len(last_len)
        