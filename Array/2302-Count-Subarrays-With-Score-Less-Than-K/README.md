# 2302. Count Subarrays With Score Less Than K


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple) ![Prefix Sum](https://img.shields.io/badge/Prefix%20Sum-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/)


## 📝 Problem Description

The **score** of an array is defined as the **product** of its sum and its length.

	- For example, the score of `[1, 2, 3, 4, 5]` is `(1 + 2 + 3 + 4 + 5) * 5 = 75`.

Given a positive integer array `nums` and an integer `k`, return *the **number of non-empty subarrays** of* `nums` *whose score is **strictly less** than* `k`.

A **subarray** is a contiguous sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [2,1,4,3,5], k = 10
**Output:** 6
**Explanation:**
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
```

Example 2:**

```

**Input:** nums = [1,1,1], k = 5
**Output:** 5
**Explanation:**
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= k <= 10^15`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a twist. It maintains a running sum of the subarray and adjusts the left boundary of the window to ensure the score of the subarray is strictly less than `k`. The key insight is to use the product of the sum and length as the score, which allows for efficient calculation and comparison.

**Approach**
1. Initialize variables `l` (left boundary), `sub_arr` (count of subarrays), `curr` (running sum), and `length` (length of the current subarray).
2. Iterate over the array with the right boundary `r`.
3. For each `r`, update `curr` by adding `nums[r]` and calculate the length of the current subarray (`length = r - l + 1`).
4. While the score of the current subarray (`curr * length`) is greater than or equal to `k`, adjust the left boundary `l` by incrementing it and subtracting `nums[l]` from `curr`. Also, decrement `length` by 1.
5. Increment `sub_arr` by the length of the current subarray (`length`) after the while loop.
6. Return `sub_arr` as the count of subarrays with score less than `k`.

**Time Complexity**
O(n), where n is the length of the input array `nums`. The while loop in step 4 is executed at most n times, and the iteration over the array is linear.

**Space Complexity**
O(1), as the solution uses a constant amount of space to store the variables `l`, `sub_arr`, `curr`, and `length`.

**Key Insight**
The solution's efficiency relies on the fact that the score of a subarray is the product of its sum and length. By maintaining a running sum and adjusting the left boundary, we can efficiently calculate the score of the subarray and count the number of subarrays with score less than `k`.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 105 ms (Beats 100%) |
| 💾 Memory | 30.7 MB (Beats 96.76%) |
| 📅 Solved | 2025-04-28 |
| 💻 Language | Python |