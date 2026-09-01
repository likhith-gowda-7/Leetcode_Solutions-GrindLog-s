class Solution:

  def minimumDeletions(self, nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
      return n

    # Find the indices of minimum and maximum elements
    min_idx = nums.index(min(nums))
    max_idx = nums.index(max(nums))

    L = min(min_idx, max_idx)
    R = max(min_idx, max_idx)

    # 1. Remove both from left
    remove_from_left = R + 1
    # 2. Remove both from right
    remove_from_right = n - L
    # 3. Remove L from left and R from right
    remove_both_ends = (L + 1) + (n - R)

    return min(remove_from_left, remove_from_right, remove_both_ends)