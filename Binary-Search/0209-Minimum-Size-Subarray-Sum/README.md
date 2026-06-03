> 📌 **Cross-listed:** Primary location is [Array/0209-Minimum-Size-Subarray-Sum](../../Array/0209-Minimum-Size-Subarray-Sum). This problem also appears under: **Array**, **Binary Search**, **Sliding Window**, **Prefix Sum**

# 209. Minimum Size Subarray Sum


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)


## 📝 Problem Description

Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a **subarray** whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

 

Example 1:**

```

**Input:** target = 7, nums = [2,3,1,2,4,3]
**Output:** 2
**Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

```

Example 2:**

```

**Input:** target = 4, nums = [1,4,4]
**Output:** 1

```

Example 3:**

```

**Input:** target = 11, nums = [1,1,1,1,1,1,1,1]
**Output:** 0

```

 

**Constraints:**

	- `1 <= target <= 10^9`

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^4`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## 🧠 Solution Explanation

## Intuition
This solution works by utilizing a sliding window approach to find the minimum length subarray whose sum is greater than or equal to the target. The key idea is to maintain a window of elements that sum up to at least the target, and then try to minimize the size of this window. By doing so, we can efficiently explore all possible subarrays and find the one with the minimum length.

## Approach
1. Initialize two pointers, `l` and `r`, to represent the left and right boundaries of the sliding window.
2. Initialize a variable `curr` to keep track of the sum of elements within the current window.
3. Iterate over the array using the `r` pointer, expanding the window to the right and updating `curr` accordingly.
4. When the sum of elements within the window is greater than or equal to the target, try to minimize the window by moving the `l` pointer to the right and updating `curr` and the result if necessary.
5. Repeat steps 3-4 until the entire array has been traversed.

## Time Complexity
The time complexity of this solution is O(n), where n is the length of the input array. This is because each element in the array is visited at most twice (once by the `r` pointer and once by the `l` pointer).

## Space Complexity
The space complexity of this solution is O(1), as it only uses a constant amount of space to store the pointers, the current sum, and the result.

## Key Insight
The key insight behind this solution is the use of a sliding window to efficiently explore all possible subarrays and find the one with the minimum length. By maintaining a window of elements that sum up to at least the target and trying to minimize its size, we can avoid unnecessary computations and achieve a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 10 ms (Beats 97.94%) |
| 💾 Memory | 20.3 MB (Beats 14.08%) |
| 📅 Solved | 2025-03-14 |
| 💻 Language | Python |