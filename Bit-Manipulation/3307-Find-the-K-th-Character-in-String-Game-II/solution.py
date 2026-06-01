class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        c=0
        val=k
        while val>1:
            jump=math.ceil(math.log2(val))
            val-=pow(2,jump-1)
            if(operations[jump-1]):
                c+=1
        return chr(ord('a')+(c%26))
            
        

