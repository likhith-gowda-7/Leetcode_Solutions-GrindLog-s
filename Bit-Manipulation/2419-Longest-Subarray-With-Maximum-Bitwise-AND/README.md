> 📌 **Cross-listed:** Primary location is [Array/2419-Longest-Subarray-With-Maximum-Bitwise-AND](../../Array/2419-Longest-Subarray-With-Maximum-Bitwise-AND). This problem also appears under: **Array**, **Bit Manipulation**, **Brainteaser**

# 2419. Longest Subarray With Maximum Bitwise AND


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Brainteaser](https://img.shields.io/badge/Brainteaser-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/)


## 📝 Problem Description

You are given an integer array `nums` of size `n`.

Consider a **non-empty** subarray from `nums` that has the **maximum** possible **bitwise AND**.

	- In other words, let `k` be the maximum value of the bitwise AND of **any** subarray of `nums`. Then, only subarrays with a bitwise AND equal to `k` should be considered.

Return *the length of the **longest** such subarray*.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A **subarray** is a contiguous sequence of elements within an array.

 

Example 1:**

```

**Input:** nums = [1,2,3,3,2,2]
**Output:** 2
**Explanation:**
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.

```

Example 2:**

```

**Input:** nums = [1,2,3,4]
**Output:** 1
**Explanation:**
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

## 🧠 Solution Explanation

**Intuition**
The solution works by tracking the maximum possible bitwise AND value and its count in the array. It iterates through the array, maintaining a counter `c` for the maximum value. Whenever it encounters the maximum value, it increments the counter; otherwise, it resets the counter to 0. The maximum count of the maximum value is the length of the longest subarray with the maximum bitwise AND.

**Approach**
1. Initialize `maxi` as the maximum value in the array `nums`.
2. Initialize `max_value_count` to 0, which will store the maximum count of the maximum value.
3. Initialize `c` to 0, which will store the current count of the maximum value.
4. Iterate through each number `n` in the array `nums`.
5. If `n` is equal to `maxi`, increment `c` by 1 and update `max_value_count` if `c` is greater than `max_value_count`.
6. If `n` is not equal to `maxi` and `c` is not 0, reset `c` to 0.
7. Return `max_value_count` as the length of the longest subarray with the maximum bitwise AND.

**Time Complexity**
O(n), where n is the size of the array `nums`. This is because we are iterating through the array once.

**Space Complexity**
O(1), which means the space complexity is constant. We are using a constant amount of space to store the maximum value, count, and other variables.

**Key Insight**
The key insight is that we only need to consider the maximum value in the array, as any subarray with a bitwise AND less than the maximum value cannot be the longest subarray with the maximum bitwise AND. By tracking the count of the maximum value, we can efficiently find the length of the longest subarray with the maximum bitwise AND.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 63 ms (Beats 7.09%) |
| 💾 Memory | 30.6 MB (Beats 100%) |
| 📅 Solved | 2025-07-31 |
| 💻 Language | Python |