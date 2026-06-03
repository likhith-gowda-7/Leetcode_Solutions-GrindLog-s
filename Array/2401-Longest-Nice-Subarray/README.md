# 2401. Longest Nice Subarray


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-nice-subarray/)


## 📝 Problem Description

You are given an array `nums` consisting of **positive** integers.

We call a subarray of `nums` **nice** if the bitwise **AND** of every pair of elements that are in **different** positions in the subarray is equal to `0`.

Return *the length of the **longest** nice subarray*.

A **subarray** is a **contiguous** part of an array.

**Note** that subarrays of length `1` are always considered nice.

 

Example 1:**

```

**Input:** nums = [1,3,8,48,10]
**Output:** 3
**Explanation:** The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
```

Example 2:**

```

**Input:** nums = [3,1,5,11,13]
**Output:** 1
**Explanation:** The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach with a twist. It maintains a running sum of the bitwise OR of elements in the current window, and expands the window to the right while ensuring that the bitwise AND of elements in different positions within the window is zero. This is achieved by maintaining a running sum of the bitwise OR of elements in the window, and shrinking the window from the left when the bitwise AND of the current element and the running sum is non-zero.

**Approach**
1. Initialize variables to keep track of the maximum length of the nice subarray (`res`), the current window's sum of bitwise OR of elements (`curr`), and the left boundary of the window (`l`).
2. Iterate over the array from the left to the right, expanding the window to the right.
3. For each new element, check if the bitwise AND of the current element and the running sum (`curr`) is non-zero.
4. If it is, shrink the window from the left by subtracting the leftmost element from the running sum (`curr`) and incrementing the left boundary (`l`).
5. Add the new element to the running sum (`curr`) and update the maximum length of the nice subarray (`res`) if necessary.
6. Repeat steps 3-5 until the end of the array is reached.

**Time Complexity**
O(n), where n is the length of the input array. This is because we are iterating over the array once, and the while loop in step 3 is bounded by the size of the window, which is at most n.

**Space Complexity**
O(1), as we are using a constant amount of space to store the variables `res`, `curr`, and `l`.

**Key Insight**
The key insight is that the bitwise OR of elements in a nice subarray is equal to the bitwise OR of the elements in the subarray minus the bitwise AND of the elements in the subarray. This allows us to maintain a running sum of the bitwise OR of elements in the window, and shrink the window from the left when the bitwise AND of the current element and the running sum is non-zero.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 77 ms (Beats 22.27%) |
| 💾 Memory | 31.8 MB (Beats 100%) |
| 📅 Solved | 2025-03-20 |
| 💻 Language | Python |