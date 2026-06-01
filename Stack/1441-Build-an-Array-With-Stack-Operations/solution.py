class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx=0
        ops=[]
        tar_length=len(target)
        for i in range(1,n+1):
            ops.append("Push")
            if(i!=target[idx]):
                ops.append("Pop")
            else:
                idx+=1
            if(idx==tar_length):
                break
        return ops