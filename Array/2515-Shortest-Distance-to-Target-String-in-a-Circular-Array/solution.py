class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if(target not in words):
            return -1
        n=len(words)
        back=startIndex
        front=startIndex
        c=0
        while words[back%n]!=target and words[front%n]!=target:
            c+=1
            front+=1
            back-=1
        return c

        
