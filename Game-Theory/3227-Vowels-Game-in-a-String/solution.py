class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """Bob can only win when there are (0) no vowels in the string(s), rest everytime Alice is going win unfortunetly....(Poor Bob)
        """
        vowels="aeiou"
        for ch in s:
            if(ch in vowels):
                return True
        return False
