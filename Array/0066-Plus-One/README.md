# 66. Plus One


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Array](https://img.shields.io/badge/Array-purple) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/plus-one/)


## 📝 Problem Description

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `i^th` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

 

Example 1:**

```

**Input:** digits = [1,2,3]
**Output:** [1,2,4]
**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

```

Example 2:**

```

**Input:** digits = [4,3,2,1]
**Output:** [4,3,2,2]
**Explanation:** The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

```

Example 3:**

```

**Input:** digits = [9]
**Output:** [1,0]
**Explanation:** The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

```

 

**Constraints:**

	- `1 <= digits.length <= 100`

	- `0 <= digits[i] <= 9`

	- `digits` does not contain any leading `0`'s.

## 🧠 Solution Explanation

## Intuition
This approach works by simulating the process of incrementing a number by one, starting from the least significant digit. When a digit is not 9, it can be incremented directly. However, when a digit is 9, it needs to be set to 0 and the next most significant digit needs to be incremented. This process continues until a non-9 digit is found or the most significant digit is reached.

## Approach
1. Initialize a flag `Change` to track whether any digit has been incremented.
2. Iterate over the input array `digits` from right to left (i.e., from least significant to most significant).
3. For each digit, check if it is not equal to 9. If so, increment the digit by 1, set `Change` to True, and break the loop.
4. If the digit is 9, set it to 0 and continue to the next most significant digit.
5. After the loop, if `Change` is still False, it means all digits were 9, so insert a new most significant digit 1 at the beginning of the array.

## Time Complexity
The time complexity is O(n), where n is the number of digits in the input array, because in the worst case, we need to iterate over all digits once.

## Space Complexity
The space complexity is O(1) in the average case, but O(n) in the worst case when all digits are 9 and a new most significant digit needs to be inserted. However, since the problem statement asks for the resulting array of digits, the output itself requires O(n) space, so the space complexity is effectively O(n).

## Key Insight
The key insight is to start from the least significant digit and propagate the carry to the next most significant digit when a digit is 9, which allows us to efficiently increment the large integer represented as an array of digits.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.3 MB (Beats 100%) |
| 📅 Solved | 2026-01-01 |
| 💻 Language | Python |