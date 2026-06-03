> 📌 **Cross-listed:** Primary location is [Array/2163-Minimum-Difference-in-Sums-After-Removal-of-Elements](../../Array/2163-Minimum-Difference-in-Sums-After-Removal-of-Elements). This problem also appears under: **Array**, **Dynamic Programming**, **Heap (Priority Queue)**

# 2163. Minimum Difference in Sums After Removal of Elements


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Heap (Priority Queue)](https://img.shields.io/badge/Heap%20(Priority%20Queue)-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/)


## 📝 Problem Description

You are given a **0-indexed** integer array `nums` consisting of `3 * n` elements.

You are allowed to remove any **subsequence** of elements of size **exactly** `n` from `nums`. The remaining `2 * n` elements will be divided into two **equal** parts:

	- The first `n` elements belonging to the first part and their sum is `sum_first`.

	- The next `n` elements belonging to the second part and their sum is `sum_second`.

The **difference in sums** of the two parts is denoted as `sum_first - sum_second`.

	- For example, if `sum_first = 3` and `sum_second = 2`, their difference is `1`.

	- Similarly, if `sum_first = 2` and `sum_second = 3`, their difference is `-1`.

Return *the **minimum difference** possible between the sums of the two parts after the removal of *`n`* elements*.

 

Example 1:**

```

**Input:** nums = [3,1,2]
**Output:** -1
**Explanation:** Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 

```

Example 2:**

```

**Input:** nums = [7,9,5,8,1,3]
**Output:** 1
**Explanation:** Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.

```

 

**Constraints:**

	- `nums.length == 3 * n`

	- `1 <= n <= 10^5`

	- `1 <= nums[i] <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution uses dynamic programming to build two arrays, `pre_arr` and `suf_arr`, which store the cumulative sums of the left and right parts of the array after removing a subsequence of size `n`. The minimum difference between the sums of the two parts is then calculated by iterating over these arrays and finding the minimum difference at each position.

**Approach**
1. Calculate the size of the subsequence `n` to be removed from the array `nums`.
2. Initialize the `left_sum` to the sum of the first `n` elements in `nums`.
3. Create a max heap `max_heap` containing the first `n` elements of `nums` with their signs flipped.
4. Build the `pre_arr` array by iterating over the remaining elements in `nums` and updating the `left_sum` by pushing the current element onto the max heap and popping the smallest element from the heap.
5. Calculate the `right_sum` to be the sum of the last `n` elements in `nums`.
6. Create a min heap `min_heap` containing the last `n` elements of `nums`.
7. Build the `suf_arr` array by iterating over the remaining elements in `nums` in reverse order and updating the `right_sum` by pushing the current element onto the min heap and popping the largest element from the heap.
8. Initialize the `res` to infinity and iterate over the `pre_arr` and `suf_arr` arrays to find the minimum difference between the sums of the two parts at each position.

**Time Complexity**
O(n log n) due to the heap operations in the `pre_arr` and `suf_arr` arrays, where n is the size of the subsequence to be removed.

**Space Complexity**
O(n) for the `pre_arr` and `suf_arr` arrays, as well as the max and min heaps.

**Key Insight**
The key insight is to use dynamic programming to build the `pre_arr` and `suf_arr` arrays, which allows us to efficiently calculate the cumulative sums of the left and right parts of the array after removing a subsequence of size `n`. This approach enables us to find the minimum difference between the sums of the two parts in O(n log n) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 280 ms (Beats 88.31%) |
| 💾 Memory | 47.6 MB (Beats 25.97%) |
| 📅 Solved | 2025-07-18 |
| 💻 Language | Python |