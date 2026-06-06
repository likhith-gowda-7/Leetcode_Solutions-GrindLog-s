# 3751. Total Waviness of Numbers in Range I


![Difficulty](https://img.shields.io/badge/Difficulty-Medium-ffc01e) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Math](https://img.shields.io/badge/Math-purple) ![Dynamic Programming](https://img.shields.io/badge/Dynamic%20Programming-purple) ![Enumeration](https://img.shields.io/badge/Enumeration-purple)


🔗 [View on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)


## 📝 Problem Description

You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

	- A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors.

	- A digit is a **valley** if it is **strictly less** than both of its immediate neighbors.

	- The first and last digits of a number **cannot** be peaks or valleys.

	- Any number with fewer than 3 digits has a waviness of 0.

Return the total sum of waviness for all numbers in the range `[num1, num2]`.
 

Example 1:**

**Input:** num1 = 120, num2 = 130

**Output:** 3

**Explanation:**

In the range `[120, 130]`:

	- `120`: middle digit 2 is a peak, waviness = 1.

	- `121`: middle digit 2 is a peak, waviness = 1.

	- `130`: middle digit 3 is a peak, waviness = 1.

	- All other numbers in the range have a waviness of 0.

Thus, total waviness is `1 + 1 + 1 = 3`.

Example 2:**

**Input:** num1 = 198, num2 = 202

**Output:** 3

**Explanation:**

In the range `[198, 202]`:

	- `198`: middle digit 9 is a peak, waviness = 1.

	- `201`: middle digit 0 is a valley, waviness = 1.

	- `202`: middle digit 0 is a valley, waviness = 1.

	- All other numbers in the range have a waviness of 0.

Thus, total waviness is `1 + 1 + 1 = 3`.

Example 3:**

**Input:** num1 = 4848, num2 = 4848

**Output:** 2

**Explanation:**

Number `4848`: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

 

**Constraints:**

	- `1 <= num1 <= num2 <= 10^5`

## 🧠 Solution Explanation

**Intuition**
The solution calculates the total waviness of numbers in a given range by iterating over each number and counting the peaks and valleys in its digits. The key insight is to recognize that the waviness of a number can be calculated by comparing each digit with its neighbors, and the solution uses a dynamic programming approach to efficiently calculate this.

**Approach**
1. Define a helper function `solve(num)` to calculate the waviness of a single number.
2. In `solve(num)`, extract the rightmost digit `right`, the current digit `curr`, and the leftmost digit `left` from the input number.
3. Initialize a variable `wave` to store the total waviness and a variable `num` to store the remaining digits of the input number.
4. Iterate over the remaining digits of the input number, comparing each digit with its neighbors and incrementing `wave` if a peak or valley is found.
5. Update `right` and `curr` to be the current and leftmost digits, respectively, for the next iteration.
6. Return the total waviness `wave`.
7. In the main function, iterate over the range of numbers from `num1` to `num2` (inclusive) and calculate the waviness of each number using the `solve(num)` function.
8. Return the total sum of waviness for all numbers in the range.

**Time Complexity**
O(n * m), where n is the number of digits in the input numbers and m is the number of numbers in the range. This is because the solution iterates over each digit in each number in the range.

**Space Complexity**
O(1), as the solution only uses a constant amount of space to store the variables `wave`, `num`, `right`, `curr`, and `left`.

**Key Insight**
The key insight is to recognize that the waviness of a number can be calculated by comparing each digit with its neighbors, and the solution uses a dynamic programming approach to efficiently calculate this. The solution also uses a clever trick to avoid iterating over the first and last digits of each number, which cannot be peaks or valleys.

## 📊 Metrics

| Metric | Value |
|:-------|:------|
| ⏱️ Runtime | 159 ms (Beats 87.46%) |
| 💾 Memory | 19.3 MB (Beats 45.45%) |
| 📅 Solved | 2026-06-04 |
| 💻 Language | Python |