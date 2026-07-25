class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = (max(nums) << 1)

        pair = [False] * mx

        # All possible pair XORs (same index allowed)
        for a in nums:
            for b in nums:
                pair[a ^ b] = True

        ans = [False] * mx

        # Extend every pair XOR with every element
        for x in range(mx):
            if pair[x]:
                for c in nums:
                    ans[x ^ c] = True

        return sum(ans)