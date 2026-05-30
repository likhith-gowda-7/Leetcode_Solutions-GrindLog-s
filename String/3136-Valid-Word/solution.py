class Solution:
    def isValid(self, word: str) -> bool:
        if(len(word)<3 or not word.isalnum()):
            return False
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        conso=0
        v=0
        d=0
        for val in word:
            if(val.isalpha()):
                if(val in vowels):
                    v+=1
                else:
                    conso+=1
            else:
                d+=1
        return True if((conso or d) and (conso and v)) else False