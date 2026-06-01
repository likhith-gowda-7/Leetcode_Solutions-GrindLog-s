class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m=len(potions)
        n=len(spells)
        pairs=[0]*n
        def bs(p):
            l=0
            r=m-1
            while l<=r:
                mid=(l+r)//2
                product=p*potions[mid]
                if(product>=success):
                    r=mid-1
                else:
                    l=mid+1
            return l
        for spell,power in enumerate(spells):
            success_idx=bs(power)
            if(success_idx==m):
                continue
            no_pairs=m-success_idx
            pairs[spell]=no_pairs
        return pairs      