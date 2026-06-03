# 869. Reordered Power of 2


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Sorting](https://img.shields.io/badge/Sorting-purple) ![Counting](https://img.shields.io/badge/Counting-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/reordered-power-of-2/)


## 📝 Problem Description

You are given an integer `n`. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return `true` *if and only if we can do this so that the resulting number is a power of two*.

 

Example 1:**

```

**Input:** n = 1
**Output:** true

```

Example 2:**

```

**Input:** n = 10
**Output:** false

```

 

**Constraints:**

	- `1 <= n <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first checking if the given number `n` is already a power of 2. If it is, the function returns `True`. Otherwise, it generates all possible powers of 2 with the same number of digits as `n` and checks if any of them have the same digit order as `n`.

**Approach**
1. Check if `n` is already a power of 2 by converting it to binary and counting the number of '1's. If there's only one '1', return `True`.
2. Convert `n` to a string, sort its digits, and store the result in `target`.
3. Initialize `till` as the largest power of 10 with `l` digits, where `l` is the length of `target`.
4. Iterate over powers of 2 from 1 to 30 (since 2^30 is the largest power of 2 with 31 digits).
5. For each power of 2 `p`, convert it to a string, sort its digits, and store the result in `curr`.
6. If `curr` matches `target`, return `True`.
7. If `p` exceeds `till`, break the loop since all remaining powers of 2 will have more digits than `n`.

**Time Complexity**
O(30 * l), where `l` is the number of digits in `n`. This is because we iterate over 30 powers of 2 and for each power, we sort its digits, which takes O(l) time.

**Space Complexity**
O(l), where `l` is the number of digits in `n`. This is because we store the sorted digits of `n` and each power of 2 in separate variables.

**Key Insight**
The key insight is that a power of 2 can have at most one '1' in its binary representation. Therefore, we can quickly check if `n` is a power of 2 by counting the number of '1's in its binary representation.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.7 MB (Beats 100%) |
| 📅 Solved | 2025-08-10 |
| 💻 Language | Python |