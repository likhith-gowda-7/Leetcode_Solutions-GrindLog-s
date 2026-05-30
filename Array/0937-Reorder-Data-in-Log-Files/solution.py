class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters=[]
        digits=[]
        for log in logs:
            iden,con=log.split(" ",1)
            if(con[0].isdigit()):
                digits.append(log)
            else:
                letters.append((con,iden,log))
        letters.sort()
        for i in range(len(letters)):
            letters[i]=letters[i][2]
        return letters+digits

        