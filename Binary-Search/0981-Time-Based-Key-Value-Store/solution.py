class TimeMap:

    def __init__(self):
        self.h1=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h1[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        value=self.h1.get(key,[])
        l=0
        r=len(value)-1
        if(value):
            while l<=r:
                mid=l+(r-l)//2
                if(value[mid][1]>timestamp):
                    r=mid-1
                else:
                    l=mid+1
            if(r>-1):
                return value[r][0]
            else:
                return ""
        else:
            return ""    