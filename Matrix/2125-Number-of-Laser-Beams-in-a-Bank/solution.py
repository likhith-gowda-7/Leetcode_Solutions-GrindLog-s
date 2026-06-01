class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cams=[]
        for floor in bank:
            sec_cam=floor.count("1")
            if(sec_cam>0):
                cams.append(sec_cam)
        total=0
        for i in range(1,len(cams)):
            total+=cams[i-1]*cams[i]
        return total