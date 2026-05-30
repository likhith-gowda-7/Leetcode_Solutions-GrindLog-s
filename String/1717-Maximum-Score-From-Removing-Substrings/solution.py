class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(arr,c1,c2,points):
            nonlocal count
            stack=[]
            for ch in arr:
                if(ch==c1 and (stack and stack[-1]==c2)):
                    stack.pop()
                    count+=points
                else:
                    stack.append(ch)
            return stack 
        find=[] 
        if(x>y):
            find=["b","a",x,y]
        else:
            find=["a","b",y,x]
        count=0
        s=remove(s,find[0],find[1],find[2])
        remove(s,find[1],find[0],find[3])
        return count
        