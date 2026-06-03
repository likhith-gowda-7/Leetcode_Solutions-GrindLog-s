# 2962. Count Subarrays Where Max Element Appears at Least K Times


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/)


## 📝 Problem Description

You are given an integer array `nums` and a **positive** integer `k`.

Return *the number of subarrays where the **maximum** element of *`nums`* appears **at least** *`k`* times in that subarray.*

A **subarray** is a contiguous sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [1,3,2,3,3], k = 2
**Output:** 6
**Explanation:** The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

```

Example 2:**

```

**Input:** nums = [1,4,2,1], k = 3
**Output:** 0
**Explanation:** No subarray contains the element 4 at least 3 times.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

	- `1 <= k <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The problem requires counting the number of subarrays where the maximum element appears at least `k` times. The key insight is to use a sliding window approach, where we maintain a count of the maximum element within the window. By expanding the window to the right and contracting it from the left, we can efficiently count the number of subarrays that meet the condition.

**Approach**
1. Initialize `maxi_num` as the maximum element in the array `nums`.
2. Initialize `ans` as 0, which will store the count of subarrays.
3. Initialize `l` as 0, which will be the left pointer of the sliding window.
4. Initialize `maxi_count` as 0, which will store the count of `maxi_num` within the window.
5. Iterate over the array `nums` with the right pointer `r`.
6. If `nums[r]` is equal to `maxi_num`, increment `maxi_count`.
7. While `maxi_count` is greater than or equal to `k`, contract the window from the left by incrementing `l`. If `nums[l]` is equal to `maxi_num`, decrement `maxi_count`.
8. Increment `ans` by `l`, which represents the number of subarrays that can be formed with the current window.
9. Return `ans` as the final count of subarrays.

**Time Complexity**
O(n), where n is the length of the array `nums`. This is because we are iterating over the array once with the sliding window approach.

**Space Complexity**
O(1), as we are using a constant amount of space to store the variables `maxi_num`, `ans`, `l`, and `maxi_count`.

**Key Insight**
The key insight is to use the sliding window approach to efficiently count the number of subarrays that meet the condition. By maintaining a count of the maximum element within the window, we can contract the window from the left and expand it to the right, allowing us to count the number of subarrays in linear time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 29.5 MB (Beats 100%) |
| 📅 Solved | 2025-05-01 |
| 💻 Language | Python |