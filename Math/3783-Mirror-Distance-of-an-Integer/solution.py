class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=int(str(n)[::-1].lstrip('0'))
        return abs(n-rev)