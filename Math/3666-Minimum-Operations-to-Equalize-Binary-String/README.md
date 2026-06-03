# 3666. Minimum Operations to Equalize Binary String


![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ff375f) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![String](https://img.shields.io/badge/String-purple) ![Breadth-First Search](https://img.shields.io/badge/Breadth--First%20Search-purple) ![Union-Find](https://img.shields.io/badge/Union--Find-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/)


## 📝 Problem Description

You are given a binary string `s`, and an integer `k`.

In one operation, you must choose **exactly** `k` **different** indices and **flip** each `'0'` to `'1'` and each `'1'` to `'0'`.

Return the **minimum** number of operations required to make all characters in the string equal to `'1'`. If it is not possible, return -1.

 

Example 1:**

**Input:** s = "110", k = 1

**Output:** 1

**Explanation:**

	- There is one `'0'` in `s`.

	- Since `k = 1`, we can flip it directly in one operation.

Example 2:**

**Input:** s = "0101", k = 3

**Output:** 2

**Explanation:**

One optimal set of operations choosing `k = 3` indices in each operation is:

	- **Operation 1**: Flip indices `[0, 1, 3]`. `s` changes from `"0101"` to `"1000"`.

	- **Operation 2**: Flip indices `[1, 2, 3]`. `s` changes from `"1000"` to `"1111"`.

Thus, the minimum number of operations is 2.

Example 3:**

**Input:** s = "101", k = 2

**Output:** -1

**Explanation:**

Since `k = 2` and `s` has only one `'0'`, it is impossible to flip exactly `k` indices to make all `'1'`. Hence, the answer is -1.

 

**Constraints:**

	- `1 <= s.length <= 10^​​​​​​​5`

	- `s[i]` is either `'0'` or `'1'`.

	- `1 <= k <= s.length`

## 🧠 Solution Explanation

**Intuition**
The solution involves calculating the minimum number of operations required to make all characters in the binary string equal to `'1'`. It takes into account the parity of the number of zeros in the string and the value of `k`, which determines the number of indices that can be flipped in each operation.

**Approach**
1. Calculate the total number of zeros in the string `s`.
2. If there are no zeros, return 0.
3. If the length of `s` is equal to `k`, return 1 if the number of zeros is equal to the length of `s`, otherwise return -1.
4. Calculate the base number of operations required to flip all zeros, assuming an even number of operations.
5. Calculate the minimum number of operations required to flip all zeros, assuming an odd number of operations.
6. If the parity of `k` and the number of zeros is the same, update the minimum number of operations to the odd case.
7. If the number of zeros is odd, update the minimum number of operations to the even case.
8. Return the minimum number of operations, or -1 if it is still infinity.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we only need to iterate over the string once to calculate the total number of zeros.

**Space Complexity**
O(1), which means the space complexity is constant. We only use a few variables to store the total number of zeros, the length of the string, and the minimum number of operations, regardless of the size of the input.

**Key Insight**
The key insight is that the minimum number of operations required to flip all zeros is determined by the parity of `k` and the number of zeros in the string. If the parity is the same, we can use an odd number of operations, otherwise we need to use an even number of operations. This insight allows us to simplify the problem and find the minimum number of operations efficiently.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 98 ms (Beats 58.1%) |
| 💾 Memory | 20.3 MB (Beats 54.29%) |
| 📅 Solved | 2026-02-27 |
| 💻 Language | Python |