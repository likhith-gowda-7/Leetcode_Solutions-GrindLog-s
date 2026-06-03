> 📌 **Cross-listed:** Primary location is [String/3258-Count-Substrings-That-Satisfy-K-Constraint-I](../../String/3258-Count-Substrings-That-Satisfy-K-Constraint-I). This problem also appears under: **String**, **Sliding Window**

# 3258. Count Substrings That Satisfy K-Constraint I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![String](https://img.shields.io/badge/String-purple) ![Sliding Window](https://img.shields.io/badge/Sliding%20Window-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/)


## 📝 Problem Description

You are given a **binary** string `s` and an integer `k`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

	- The number of `0`'s in the string is at most `k`.

	- The number of `1`'s in the string is at most `k`.

Return an integer denoting the number of substrings of `s` that satisfy the **k-constraint**.

 

Example 1:**

**Input:** s = "10101", k = 1

**Output:** 12

**Explanation:**

Every substring of `s` except the substrings `"1010"`, `"10101"`, and `"0101"` satisfies the k-constraint.

Example 2:**

**Input:** s = "1010101", k = 2

**Output:** 25

**Explanation:**

Every substring of `s` except the substrings with a length greater than 5 satisfies the k-constraint.

Example 3:**

**Input:** s = "11111", k = 1

**Output:** 15

**Explanation:**

All substrings of `s` satisfy the k-constraint.

 

**Constraints:**

	- `1 <= s.length <= 50 `

	- `1 <= k <= s.length`

	- `s[i]` is either `'0'` or `'1'`.

## 🧠 Solution Explanation

**Intuition**
The solution uses a sliding window approach to count the number of substrings that satisfy the k-constraint. By maintaining two counters for zeros and ones, it can efficiently track the number of substrings that violate the constraint and skip over them.

**Approach**
1. Initialize two counters, `zero_count` and `one_count`, to keep track of the number of zeros and ones in the current window.
2. Initialize the result counter `res` to 0 and the left pointer `l` to 0.
3. Iterate over the string `s` using the right pointer `r`.
4. For each character, increment the corresponding counter (`one_count` for '1' or `zero_count` for '0').
5. If both counters exceed `k`, slide the window to the right by incrementing `l` and decrementing the corresponding counter.
6. For each valid window, increment the result counter `res` by the window size (`r - l + 1`).
7. Return the total count of valid substrings.

**Time Complexity**
O(n), where n is the length of the string `s`. This is because we only iterate over the string once, using a single pass through the characters.

**Space Complexity**
O(1), since we only use a constant amount of space to store the counters and pointers, regardless of the input size.

**Key Insight**
The key insight is that we can efficiently skip over invalid substrings by maintaining a sliding window and tracking the number of zeros and ones within it. This allows us to count the number of valid substrings in linear time, making the solution efficient for large inputs.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 3 ms (Beats 78.55%) |
| 💾 Memory | 18 MB (Beats 100%) |
| 📅 Solved | 2025-03-11 |
| 💻 Language | Python |