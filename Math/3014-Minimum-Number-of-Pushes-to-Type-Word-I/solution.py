class Solution:
    def minimumPushes(self, word: str) -> int:
        '''Imp Note: Since all chars in words are unique and 
        the keypad phone has only 8 keys for char attachment, So do it in 
        Greedy Way>>>'''
        n=len(word)
        res=0
        '''Idea is to Assign any 8 chars to the first press of any 8 button, 
        And then another 8 chars to the 2 presses of any 8 button 
        and then another 8 for 3rd press and so on.....''' 
        presses=1
        while n>=8:
            res+=(8*presses)
            presses+=1
            n-=8
        res+=(n*presses)
        return res
            