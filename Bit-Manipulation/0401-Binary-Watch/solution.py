class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        for hour in range(12):
            for minute in range(60):
                bit_cnt=bin(hour).count("1")+bin(minute).count("1")
                if(bit_cnt==turnedOn):
                    time=f"{hour}:{minute:02d}"
                    res.append(time)
        return res