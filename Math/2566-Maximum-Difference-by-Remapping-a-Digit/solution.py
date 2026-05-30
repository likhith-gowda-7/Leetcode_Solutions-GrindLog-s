class Solution:
    def minMaxDifference(self, num: int) -> int:
        number=str(num)
        def check(s,change,find):
            val=""
            for i in s:
                if(change==None and i!=find):
                    change=i
                if(change!=None and i==change):
                    val+=find
                    continue
                val+=i
            return int(val)
        return check(number,None,"9")-check(number,None,"0")

            
        
        
        