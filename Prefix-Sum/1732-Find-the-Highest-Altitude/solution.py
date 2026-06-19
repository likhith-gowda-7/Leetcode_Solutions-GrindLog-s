class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        rise=0
        max_rise=0
        for alti in gain:
            rise+=alti
            max_rise=max(max_rise,rise)
        return max_rise