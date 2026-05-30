class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sl=blocks[:k].count("W")
        mini=sl
        for i in range(k,len(blocks)):
            if(blocks[i-k]=="W"):
                sl-=1
            if(blocks[i]=="W"):
                sl+=1
            mini=min(mini,sl)
        return mini

