class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good=-1
        c=1
        for i in range(1,len(num)):
            if(num[i-1]==num[i]):
                c+=1
                if(c==3):
                    max_good=max(max_good,int(num[i]))
            else:
                c=1
        return str(max_good)*3 if(max_good!=-1) else ""
        