# 3754. Concatenate Non-Zero Digits and Multiply by Sum I


![Difficulty](https://img.shields.io/badge/Difficulty-Easy-00b8a3) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/)


## 📝 Problem Description

You are given an integer `n`.

Form a new integer `x` by concatenating all the **non-zero digits** of `n` in their original order. If there are no **non-zero** digits, `x = 0`.

Let `sum` be the **sum of digits** in `x`.

Return an integer representing the value of `x * sum`.

 

Example 1:**

**Input:** n = 10203004

**Output:** 12340

**Explanation:**

	- The non-zero digits are 1, 2, 3, and 4. Thus, `x = 1234`.

	- The sum of digits is `sum = 1 + 2 + 3 + 4 = 10`.

	- Therefore, the answer is `x * sum = 1234 * 10 = 12340`.

Example 2:**

**Input:** n = 1000

**Output:** 1

**Explanation:**

	- The non-zero digit is 1, so `x = 1` and `sum = 1`.

	- Therefore, the answer is `x * sum = 1 * 1 = 1`.

 

**Constraints:**

	- `0 <= n <= 10^9`

## 🧠 Solution Explanation

**Intuition**
The solution works by first reversing the input integer `n` to process its digits from right to left. It then iterates through the digits, adding non-zero digits to the sum and concatenating them to form the new integer `x`. Finally, it returns the product of `x` and the sum of its digits.

**Approach**
1. Convert the input integer `n` to a string, reverse it, and convert it back to an integer to process its digits from right to left.
2. Initialize variables `digit_sum` to store the sum of non-zero digits and `x` to store the concatenated non-zero digits.
3. Iterate through the digits of `n` from right to left:
   - Get the last digit `last` by taking the remainder of `n` divided by 10.
   - If `last` is not zero, add it to `digit_sum` and concatenate it to `x` by multiplying `x` by 10 and adding `last`.
   - Remove the last digit from `n` by performing integer division by 10.
4. After iterating through all digits, remove the trailing zero from `x` by performing integer division by 10.
5. Return the product of `x` and `digit_sum`.

**Time Complexity**
O(log(n)) because we are processing each digit of the input integer `n` once, and the number of digits is logarithmic in the size of the input.

**Space Complexity**
O(1) because we are using a constant amount of space to store the sum of non-zero digits and the concatenated non-zero digits, regardless of the size of the input.

**Key Insight**
The key insight is to process the digits of the input integer from right to left, which allows us to easily concatenate non-zero digits and calculate the sum of their digits. This approach avoids the need for explicit string manipulation and makes the solution efficient.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 0 ms (Beats 100%) |
| 💾 Memory | 19.2 MB (Beats 51.25%) |
| 📅 Solved | 2026-07-07 |
| 💻 Language | Python |