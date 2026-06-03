> 📌 **Cross-listed:** Primary location is [Hash Table/0202-Happy-Number](../../Hash-Table/0202-Happy-Number). This problem also appears under: **Hash Table**, **Math**, **Two Pointers**

# 202. Happy Number


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Hash Table](https://img.shields.io/badge/Hash%20Table-purple) ![Math](https://img.shields.io/badge/Math-purple) ![Two Pointers](https://img.shields.io/badge/Two%20Pointers-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/happy-number/)


## 📝 Problem Description

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

	- Starting with any positive integer, replace the number by the sum of the squares of its digits.

	- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.

	- Those numbers for which this process **ends in 1** are happy.

Return `true` *if* `n` *is a happy number, and* `false` *if not*.

 

Example 1:**

```

**Input:** n = 19
**Output:** true
**Explanation:**
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

```

Example 2:**

```

**Input:** n = 2
**Output:** false

```

 

**Constraints:**

	- `1 <= n <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The solution uses a set to keep track of the numbers we've seen so far, which allows us to detect cycles. This is crucial because a happy number will eventually reach 1, while a non-happy number will get stuck in a cycle.

**Approach**
1. Define a helper function `power_of_numbers(n)` that calculates the sum of squares of the digits of `n`.
2. Initialize a set `seen` to store the numbers we've seen so far.
3. While `n` is not equal to 1, check if `n` is in the `seen` set. If it is, return `False` because we've encountered a cycle.
4. Add `n` to the `seen` set and update `n` to be the result of `power_of_numbers(n)`.
5. Repeat steps 3-4 until `n` equals 1, at which point return `True`.

**Time Complexity**
O(log(n)) because in the worst case, we're reducing the number of digits by one in each iteration. Since the number of digits in a number is proportional to the logarithm of the number, the time complexity is logarithmic.

**Space Complexity**
O(log(n)) because in the worst case, we're storing all numbers in the `seen` set, which has a size proportional to the logarithm of the input number.

**Key Insight**
The key insight is that we can use a set to detect cycles, which allows us to determine whether a number is happy or not. This approach is much more efficient than trying to calculate the sum of squares of the digits repeatedly, which would lead to an exponential time complexity.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.8 MB (Beats 100%) |
| 📅 Solved | 2025-11-20 |
| 💻 Language | Python |