class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_count=moves.count("L")
        right_count=moves.count("R")
        choices_count=moves.count("_")
        return (max(left_count,right_count)+choices_count)-min(left_count,right_count)