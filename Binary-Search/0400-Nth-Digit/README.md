> 📌 **Cross-listed:** Primary location is [Math/0400-Nth-Digit](../../Math/0400-Nth-Digit). This problem also appears under: **Math**, **Binary Search**

# 400. Nth Digit


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Binary Search](https://img.shields.io/badge/Binary%20Search-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/nth-digit/)


## 📝 Problem Description

Given an integer `n`, return the `n^th` digit of the infinite integer sequence `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]`.

 

Example 1:**

```

**Input:** n = 3
**Output:** 3

```

Example 2:**

```

**Input:** n = 11
**Output:** 0
**Explanation:** The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

```

 

**Constraints:**

	- `1 <= n <= 2^31 - 1`

## 🧠 Solution Explanation

**Intuition**
The solution utilizes a clever binary search-like approach to find the `n^th` digit of the infinite integer sequence. It breaks down the problem into smaller groups of numbers with the same number of digits, and then finds the group that contains the `n^th` digit.

**Approach**
1. If `n` is less than 10, return `n` directly since it's a single-digit number.
2. Initialize variables `d` (number of digits in the current group) and `count` (total numbers in the group) to 1 and 9, respectively.
3. While `n` is greater than the total digits covered in the current group (`d * count`):
   - Subtract the digits covered in this group from `n`.
   - Increment `d` to move to the next digit group.
   - Multiply `count` by 10 to account for the next group having 10 times more numbers.
4. Calculate the index of the group that contains the `n^th` digit (`group_ind`).
5. Calculate the starting number of the group (`start_ind`) and the target number that contains the `n^th` digit (`target`).
6. Calculate the index of the digit within the target number (`res_ind`).
7. Extract the `n^th` digit from the target number and return it.

**Time Complexity**
O(log(n)) due to the while loop that iterates until `n` is covered by the current group. The number of iterations is proportional to the logarithm of `n` because each iteration effectively doubles the size of the group.

**Space Complexity**
O(1) since the solution only uses a constant amount of space to store the variables `d`, `count`, `num`, `group_ind`, `start_ind`, `target`, and `res_ind`.

**Key Insight**
The key insight is to break down the problem into smaller groups of numbers with the same number of digits, and then use a binary search-like approach to find the group that contains the `n^th` digit. This approach allows the solution to efficiently find the `n^th` digit in O(log(n)) time.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.3 MB (Beats 100%) |
| 📅 Solved | 2025-12-29 |
| 💻 Language | Python |