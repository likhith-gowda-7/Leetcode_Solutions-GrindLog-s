class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h={}
        for num in arr:
            if(num in h):
                h[num]+=1
            else:
                h[num]=1
        return len(h)==len(set(h.values()))
        