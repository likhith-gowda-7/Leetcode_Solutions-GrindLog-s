class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n=len(encodedText)
        if(n==0):
            return encodedText
        cols=n//rows
        matrix=[["#"]*cols for _ in range(rows)]
        idx=0
        for i in range(rows):
            if(idx==n):
                break
            for j in range(cols):
                matrix[i][j]=encodedText[idx]
                idx+=1
                if(idx==n):
                    break
        res=[]
        for i in range(cols):
            row=0
            col=i
            while row<rows and col<cols:
                val=matrix[row][col]
                if(val!="#"):
                    res.append(val)
                row+=1
                col+=1
        while res[-1]==" ":
            res.pop()
        return "".join(res)
