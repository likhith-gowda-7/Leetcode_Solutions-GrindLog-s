class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n=len(word)
        upper_count=0
        lower_count=0
        for w in word:
            if(ord(w)>96):
                lower_count+=1
            else:
                upper_count+=1
        return (upper_count==n or lower_count==n or (word[0]==word[0].upper() and lower_count==n-1))