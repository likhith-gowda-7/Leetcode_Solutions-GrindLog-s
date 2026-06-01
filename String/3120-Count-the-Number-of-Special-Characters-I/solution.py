class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        h1=Counter(word)
        count=0
        for key in h1.keys():
            if(ord(key)<97 and key.lower() in h1):
                count+=1
            elif(ord(key)>96 and key.upper() in h1):
                count+=1
        return count//2