class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # If needle is an empty string, return 0
            return 0
        nl=len(needle)
        for i in range(len(haystack)):
            ch=haystack[i:i+nl]
            if(ch==needle):
                return i
        return -1
