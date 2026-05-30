class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiou"
        l=list(s)
        i,j=0,len(s)-1
        while(i<j):
            if(l[j].lower() not in vowels):
                j-=1
            elif(l[i].lower() not in vowels):
                i+=1
            elif(l[i].lower() in vowels and l[j].lower() in vowels):
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
        return "".join(l)

                
            


        
