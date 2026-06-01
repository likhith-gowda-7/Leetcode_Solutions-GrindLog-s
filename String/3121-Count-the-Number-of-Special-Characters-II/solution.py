class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_count=defaultdict(int)
        res=0
        for i in range(len(word)):
            if(word[i].islower() or word[i] not in char_count):
                char_count[word[i]]=i
        for key,val in char_count.items():
            if(key.isupper() and key.lower() in char_count):
                last_idx=char_count[key.lower()]
                first_idx=val
                if(first_idx>last_idx):
                    res+=1
        return res
        
        
        