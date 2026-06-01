class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        curr=0
        left=0
        maxi_count=0
        for right in range(len(fruits)):
            curr+=fruits[right][1]
            while left<=right:
                l_pos=fruits[left][0]
                r_pos=fruits[right][0]
                min_steps=min(abs(startPos-l_pos)+(r_pos-l_pos),abs(startPos-r_pos)+(r_pos-l_pos))
                if(min_steps<=k):
                    break
                curr-=fruits[left][1]
                left+=1
            maxi_count=max(maxi_count,curr)
        return maxi_count