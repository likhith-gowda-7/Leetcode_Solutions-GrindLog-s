class Solution:
    def sortVowels(self, s: str) -> str:
        n=len(s)
        vowels="AEIOUaeiou"
        vow_map=defaultdict(int)
        res=[""]*n
        vow_indexes=[]
        for i,ch in enumerate(s):
            if(ch in vowels):
                vow_map[ch]+=1
                vow_indexes.append(i)
            else:
                res[i]=ch
        i=0
        for vow in vowels:
            if(vow in vow_map):
                for _ in range(vow_map[vow]):
                    idx=vow_indexes[i]
                    res[idx]=vow
                    i+=1
        return "".join(res)
            
