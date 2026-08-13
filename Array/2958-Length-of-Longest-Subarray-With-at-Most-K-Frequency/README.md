# 2958. Length of Longest Subarray With at Most K Frequency


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/)


## 📝 Problem Description

You are given an integer array `nums` and an integer `k`.

The **frequency** of an element `x` is the number of times it occurs in an array.

An array is called **good** if the frequency of each element in this array is **less than or equal** to `k`.

Return *the length of the **longest** **good** subarray of* `nums`*.*

A **subarray** is a contiguous non-empty sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [1,2,3,1,2,3,1,2], k = 2
**Output:** 6
**Explanation:** The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.

```

Example 2:**

```

**Input:** nums = [1,2,1,2,1,2,1,2], k = 1
**Output:** 2
**Explanation:** The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
It can be shown that there are no good subarrays with length more than 2.

```

Example 3:**

```

**Input:** nums = [5,5,5,5,5,5,5], k = 4
**Output:** 4
**Explanation:** The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
It can be shown that there are no good subarrays with length more than 4.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= k <= nums.length`

## 🧠 Solution Explanation

**Intuition**
The problem requires finding the longest subarray where the frequency of each element is less than or equal to a given number `k`. The key insight is to use a sliding window approach, maintaining a frequency count of elements within the current window. By expanding the window to the right and shrinking it from the left when the frequency of an element exceeds `k`, we can efficiently find the longest good subarray.

**Approach**
1. Initialize a frequency dictionary `freq` to keep track of element frequencies, a left pointer `l`, and a result variable `res` to store the maximum subarray length.
2. Iterate over the array with a right pointer `r`, incrementing the frequency of the current element and the subarray length `sub_len`.
3. If the frequency of the current element exceeds `k`, decrement the frequency of the leftmost element and the subarray length, moving the left pointer `l` to the right.
4. Update the result `res` if the current subarray length is greater than the maximum length found so far.
5. Repeat steps 2-4 until the right pointer reaches the end of the array.

**Time Complexity**
O(n), where n is the length of the input array. This is because we make a single pass through the array, with each element being processed at most twice (once when entering the window and once when leaving).

**Space Complexity**
O(n), where n is the length of the input array. This is because we need to store the frequency of each element in the frequency dictionary.

**Key Insight**
The key to this solution is the sliding window approach, which allows us to efficiently find the longest good subarray by maintaining a balance between expanding the window to the right and shrinking it from the left. This approach ensures that we process each element at most twice, resulting in a linear time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 237 ms (Beats 89.63%) |
| 💾 Memory | 35.2 MB (Beats 72.73%) |
| 📅 Solved | 2026-08-12 |
| 💻 Language | Python |