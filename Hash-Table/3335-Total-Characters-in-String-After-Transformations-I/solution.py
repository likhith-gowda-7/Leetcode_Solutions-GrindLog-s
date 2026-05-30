class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod=10**9+7
        #making it deque becoz its faster
        freq=deque([0]*26)
        for i in s:
            ind=ord(i)-97
            freq[ind]+=1
        #here we remove the z's value(last index) and add to a(just append it at front) and for b we'll add it in 1 index
        for _ in range(t):
            val=freq.pop()
            freq.appendleft(val)
            freq[1]+=val
        #we return sum of freq,the sum could become large so we'll mod it to reduce it 
        return sum(freq)%mod


        