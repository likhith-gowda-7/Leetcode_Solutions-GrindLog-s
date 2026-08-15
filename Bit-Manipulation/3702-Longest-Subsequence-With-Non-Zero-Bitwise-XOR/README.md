> 📌 **Cross-listed:** Primary location is [Array/3702-Longest-Subsequence-With-Non-Zero-Bitwise-XOR](../../Array/3702-Longest-Subsequence-With-Non-Zero-Bitwise-XOR). This problem also appears under: **Array**, **Bit Manipulation**

# 3702. Longest Subsequence With Non-Zero Bitwise XOR


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Bit Manipulation](https://img.shields.io/badge/Bit%20Manipulation-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/)


## 📝 Problem Description

You are given an integer array `nums`.

Return the length of the **longest subsequence** in `nums` whose bitwise **XOR** is **non-zero**. If no such **subsequence** exists, return 0.

 

Example 1:**

**Input:** nums = [1,2,3]

**Output:** 2

**Explanation:**

One longest subsequence is `[2, 3]`. The bitwise XOR is computed as `2 XOR 3 = 1`, which is non-zero.

Example 2:**

**Input:** nums = [2,3,4]

**Output:** 3

**Explanation:**

The longest subsequence is `[2, 3, 4]`. The bitwise XOR is computed as `2 XOR 3 XOR 4 = 5`, which is non-zero.

 

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `0 <= nums[i] <= 10^9`

## 🧠 Solution Explanation

**Intuition**  
If the XOR of the whole array is non‑zero, the entire array is already a valid subsequence.  
If the total XOR is zero, removing any single element that is non‑zero will make the XOR non‑zero, because the XOR of the remaining elements equals the removed element.  
If every element is zero, no subsequence can have a non‑zero XOR.

**Approach**  
1. Let `n` be the length of `nums`.  
2. If all elements are `0`, return `0`.  
3. Compute `x = nums[0] ^ nums[1] ^ … ^ nums[n‑1]`.  
4. If `x` is non‑zero, return `n`.  
5. Otherwise (total XOR is zero), return `n‑1` (drop any non‑zero element).

**Time Complexity**  
`O(n)` – a single pass to check for all zeros and another pass to compute the XOR.

**Space Complexity**  
`O(1)` – only a few integer variables are used, regardless of input size.

**Key Insight**  
A non‑zero total XOR means the whole array works; a zero total XOR can be fixed by dropping one element, and if all elements are zero no solution exists. This reduces the problem to a constant‑time decision after a linear scan.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 26 ms (Beats 75.81%) |
| 💾 Memory | 33.9 MB (Beats 34.68%) |
| 📅 Solved | 2026-08-15 |
| 💻 Language | Python |