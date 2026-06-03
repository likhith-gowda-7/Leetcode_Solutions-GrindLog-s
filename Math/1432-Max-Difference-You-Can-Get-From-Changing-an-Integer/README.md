# 1432. Max Difference You Can Get From Changing an Integer


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Greedy](https://img.shields.io/badge/Greedy-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)


## 📝 Problem Description

You are given an integer `num`. You will apply the following steps to `num` **two** separate times:

	- Pick a digit `x (0 <= x <= 9)`.

	- Pick another digit `y (0 <= y <= 9)`. Note `y` can be equal to `x`.

	- Replace all the occurrences of `x` in the decimal representation of `num` by `y`.

Let `a` and `b` be the two results from applying the operation to `num` *independently*.

Return *the max difference* between `a` and `b`.

Note that neither `a` nor `b` may have any leading zeros, and **must not** be 0.

 

Example 1:**

```

**Input:** num = 555
**Output:** 888
**Explanation:** The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

```

Example 2:**

```

**Input:** num = 9
**Output:** 8
**Explanation:** The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

```

 

**Constraints:**

	- `1 <= num <= 10^8`

## 🧠 Solution Explanation

**Intuition**
The solution works by finding the maximum possible difference between two integers obtained by replacing digits in the input number. The key insight is to maximize the difference by replacing the largest digit with 9 and the smallest digit with 1, or vice versa.

**Approach**
1. Convert the input number to a string to easily access and replace individual digits.
2. Define a helper function `check` that takes the number string, a digit to replace (initially `None`), a replacement digit (initially "9"), and a flag to indicate whether to replace the digit.
3. Iterate through the number string, replacing the digit if the flag is `True` and the digit is less than 9, or if the digit is greater than 1 and the flag is `False`.
4. Return the integer value of the modified number string.
5. Call the `check` function twice: once to replace the largest digit with 9 and once to replace the smallest digit with 1 (or vice versa), and return the difference between the two results.

**Time Complexity**
O(n), where n is the number of digits in the input number. This is because we iterate through the number string once to replace the digits.

**Space Complexity**
O(n), where n is the number of digits in the input number. This is because we create a new string to store the modified number.

**Key Insight**
The key to this solution is to maximize the difference by replacing the largest digit with 9 and the smallest digit with 1 (or vice versa). This is achieved by carefully selecting the replacement digits and using a flag to control the replacement process.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 17.6 MB (Beats 100%) |
| 📅 Solved | 2025-06-15 |
| 💻 Language | Python |