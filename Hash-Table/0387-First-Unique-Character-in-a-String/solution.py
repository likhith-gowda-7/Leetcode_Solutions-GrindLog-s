class Solution:
    def firstUniqChar(self, s: str) -> int:
        h1=Counter(s)
        for key,val in h1.items():
            if(val<2):
                return s.find(key)
        return -1
        
        