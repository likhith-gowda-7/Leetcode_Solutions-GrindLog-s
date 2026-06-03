> 📌 **Cross-listed:** Primary location is [Math/0788-Rotated-Digits](../../Math/0788-Rotated-Digits). This problem also appears under: **Math**, **Dynamic Programming**

# 788. Rotated Digits


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/rotated-digits/)


## 📝 Problem Description

An integer `x` is a **good** if after rotating each digit individually by 180 degrees, we get a valid number that is different from `x`. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

	- `0`, `1`, and `8` rotate to themselves,

	- `2` and `5` rotate to each other (in this case they are rotated in a different direction, in other words, `2` or `5` gets mirrored),

	- `6` and `9` rotate to each other, and

	- the rest of the numbers do not rotate to any other number and become invalid.

Given an integer `n`, return *the number of **good** integers in the range *`[1, n]`.

 

Example 1:**

```

**Input:** n = 10
**Output:** 4
**Explanation:** There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

```

Example 2:**

```

**Input:** n = 1
**Output:** 0

```

Example 3:**

```

**Input:** n = 2
**Output:** 1

```

 

**Constraints:**

	- `1 <= n <= 10^4`

## 🧠 Solution Explanation

**Intuition**
The problem asks us to count the number of integers in the range `[1, n]` that are "good" according to a specific definition. A number is "good" if it can be rotated by 180 degrees to form a different valid number. The solution uses a dynamic programming approach to efficiently calculate the number of good integers.

**Approach**
1. Define a set `valid` containing the digits that rotate to themselves or to a different valid digit (2, 5, 6, 9).
2. Create a helper function `rev(num)` that checks if a given number can be rotated to form a good integer.
   - If the last digit of the number is 3, 4, or 7, return 0 because these digits cannot be rotated to form a valid number.
   - If the last digit is in the `valid` set, increment a `change` counter.
   - Remove the last digit from the number and repeat the process until the number is exhausted.
   - Return the `change` counter, which indicates the number of valid rotations.
3. Initialize a `total` counter to store the number of good integers.
4. Iterate over the range `[1, n]` and call the `rev(number)` function for each number.
5. Increment the `total` counter by the result of `rev(number)` for each number.
6. Return the final value of `total`.

**Time Complexity**
O(n log n) because the `rev(num)` function iterates over the digits of each number, and the loop iterates over the range `[1, n]`.

**Space Complexity**
O(1) because the `valid` set and the `total` counter are constant-sized variables.

**Key Insight**
The key insight is to recognize that the problem can be solved by iterating over the range `[1, n]` and checking each number individually. The dynamic programming approach used in the solution allows us to efficiently calculate the number of good integers by counting the valid rotations for each number.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 27 ms (Beats 57.26%) |
| 💾 Memory | 19.4 MB (Beats 31.06%) |
| 📅 Solved | 2026-05-02 |
| 💻 Language | Python |