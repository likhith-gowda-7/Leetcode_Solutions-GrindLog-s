class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h1=Counter(nums)
        max_freq=max(h1.values())
        freq_arr=[[] for _ in range(max_freq+1)]
        for key,freq in h1.items():
            freq_arr[freq].append(key)
        res=[]
        length=0
        for i in range(max_freq,0,-1):
            while freq_arr[i]:
                if(length==k):
                    return res
                val=freq_arr[i].pop()
                res.append(val)
                length+=1
        return res
