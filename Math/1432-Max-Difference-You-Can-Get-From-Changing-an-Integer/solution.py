class Solution:
    def maxDiff(self, num: int) -> int:
        number=str(num)
        def check(number,change,find,do_it):
            val=""
            for i in range(len(number)):
                n=int(number[i])
                if(do_it):
                    if(change==None and n<9):
                        change=number[i]
                elif(change==None):
                        if(i==0 and n>1):
                            find="1"
                            change=number[i]
                        elif(i!=0 and n>1):
                            change=number[i]
                if(change!=None and number[i]==change):
                    val+=find
                    continue
                val+=number[i]
            return int(val)
        return check(number,None,"9",True)-check(number,None,"0",False)